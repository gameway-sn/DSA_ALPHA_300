"""
SRM Alpha 300 Placement Training - Problem & Repository Manager
Automates folder lookup, solution placement, and README.md generation according to curriculum rules.
"""

import os
import sys
import json
import re
import subprocess
from datetime import datetime

CURRICULUM_FILE = os.path.join(os.path.dirname(os.path.abspath(__file__)), "curriculum_mapping.json")

def load_curriculum():
    with open(CURRICULUM_FILE, "r", encoding="utf-8") as f:
        return json.load(f)

def find_day(month=None, day=None, query=None):
    """
    Find matching day details in the curriculum.
    Can search by:
      - month (e.g. 'oct', 'nov', 'dec') and day (e.g. 22, '22-oct')
      - query string (e.g. 'Two Sum', 'binary search', '22 oct')
    """
    curriculum = load_curriculum()

    if month and day:
        month_key = month.lower()[:3]
        day_str = f"{int(day):02d}-{month_key}"
        if month_key in curriculum:
            for week_key, week_val in curriculum[month_key]["weeks"].items():
                if day_str in week_val["days"]:
                    return {
                        "month": month_key,
                        "week": week_key,
                        "day_folder": day_str,
                        "info": week_val["days"][day_str]
                    }

    if query:
        q = query.lower().strip()
        # Check date patterns like '22 oct', '22-oct', 'oct 22', 'oct-22'
        m = re.search(r'(\d{1,2})[\s\-]+(oct|nov|dec)', q)
        if not m:
            m = re.search(r'(oct|nov|dec)[\s\-]+(\d{1,2})', q)
            if m:
                month_found, day_found = m.group(1), m.group(2)
                return find_day(month=month_found, day=day_found)
        else:
            day_found, month_found = m.group(1), m.group(2)
            return find_day(month=month_found, day=day_found)

        # Check by problem name
        for m_key, m_val in curriculum.items():
            for w_key, w_val in m_val["weeks"].items():
                for d_key, d_val in w_val["days"].items():
                    for idx, prob in enumerate(d_val["problems"]):
                        if q in prob.lower():
                            return {
                                "month": m_key,
                                "week": w_key,
                                "day_folder": d_key,
                                "problem_index": idx + 1,
                                "problem_name": prob,
                                "info": d_val
                            }
    return None

def sanitize_filename(name):
    clean = re.sub(r'[^a-zA-Z0-9]+', '_', name.strip().lower()).strip('_')
    return clean

def save_solution(month, day, problem_num, code, approach="", time_comp="", space_comp="", edge_case="", problem_name=""):
    """
    Saves solution code and updates day README.md in the exact required folder structure.
    """
    match = find_day(month=month, day=day)
    if not match:
        raise ValueError(f"Could not find matching curriculum entry for Month={month}, Day={day}")

    target_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), match["month"], match["week"], match["day_folder"])
    os.makedirs(target_dir, exist_ok=True)

    info = match["info"]
    prob_list = info.get("problems", [])
    p_num = int(problem_num)
    if not problem_name:
        if 1 <= p_num <= len(prob_list):
            problem_name = prob_list[p_num - 1]
        else:
            problem_name = f"Problem {p_num}"

    safe_name = sanitize_filename(problem_name)
    code_filename = f"problem_{p_num}_{safe_name}.py"
    code_filepath = os.path.join(target_dir, code_filename)

    with open(code_filepath, "w", encoding="utf-8") as f:
        f.write(code.strip() + "\n")

    # Generate or update README.md
    readme_path = os.path.join(target_dir, "README.md")
    existing_content = ""
    if os.path.exists(readme_path):
        with open(readme_path, "r", encoding="utf-8") as f:
            existing_content = f.read()

    # Create problem section
    new_prob_section = f"""### Problem {p_num}: {problem_name}
- **Solution File**: [`{code_filename}`](./{code_filename})
- **Approach**:
  {approach if approach else 'Direct implementation from primitives without library helpers.'}
- **Time Complexity**: `{time_comp if time_comp else 'O(N)'}`
- **Space Complexity**: `{space_comp if space_comp else 'O(1)'}`
- **Edge Case Missed on First Attempt**:
  {edge_case if edge_case else 'Handling boundary conditions, duplicates, or empty/single inputs.'}
"""

    if not existing_content:
        header = f"""# Day {info['day_number']} · {match['day_folder']} ({info['day_of_week']})

**Topic**: {info['topic']}  
**DON'T REACH FOR**: `{info['dont_reach_for']}`

---

## 📝 Problems & Solutions

"""
        footer = f"""
---

## 💬 Discord Submission Command
```text
/done day{info['day_number']} <github-link-to-problem-1> <github-link-to-problem-2> <github-link-to-problem-3>
```
"""
        final_readme = header + new_prob_section + "\n" + footer
    else:
        # Check if Problem section already exists
        pattern = rf"(### Problem {p_num}:.*?)(?=### Problem|\Z|---\n\n## 💬 Discord)"
        if re.search(pattern, existing_content, flags=re.DOTALL):
            final_readme = re.sub(pattern, new_prob_section + "\n", existing_content, flags=re.DOTALL)
        else:
            insert_pos = existing_content.find("---\n\n## 💬 Discord")
            if insert_pos != -1:
                final_readme = existing_content[:insert_pos] + new_prob_section + "\n" + existing_content[insert_pos:]
            else:
                final_readme = existing_content + "\n" + new_prob_section

    with open(readme_path, "w", encoding="utf-8") as f:
        f.write(final_readme)

    return {
        "folder": target_dir,
        "code_path": code_filepath,
        "readme_path": readme_path,
        "relative_folder": f"{match['month']}/{match['week']}/{match['day_folder']}",
        "code_filename": code_filename,
        "day_number": info['day_number']
    }

def git_commit_and_push(commit_msg):
    """Commits all changes and pushes if a remote is configured."""
    subprocess.run(["git", "add", "."], check=True)
    subprocess.run(["git", "commit", "-m", commit_msg], check=True)
    # Check if remote exists
    remotes = subprocess.run(["git", "remote"], capture_output=True, text=True).stdout.strip()
    if remotes:
        subprocess.run(["git", "push", "origin", "main"], check=False)

if __name__ == "__main__":
    if len(sys.argv) > 1:
        q = " ".join(sys.argv[1:])
        res = find_day(query=q)
        if res:
            print(json.dumps(res, indent=2))
        else:
            print(f"No match found for: {q}")
    else:
        print("Usage: python problem_manager.py '<date or problem name>'")
