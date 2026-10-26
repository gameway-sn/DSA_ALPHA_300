# Agent Instructions: SRM Alpha 300 DSA Automation

> **CRITICAL INSTRUCTION FOR ANY AGENT OPENING THIS WORKSPACE**:
> The user will paste code solutions into the chat (often with minimal or no additional explanation). 
> Your job is to **AUTOMATICALLY** detect the problem, place the solution in the correct folder, generate the required `README.md`, and push to GitHub.

---

## ⚡ The Zero-Friction Workflow

When the user pastes code into chat:

1. **Identify the Problem & Date**:
   - Inspect the class/function names (e.g., `twoSum`, `searchInsert`, `firstBadVersion`, `maxSubArray`, etc.) or date keywords in the user's message.
   - Run the lookup command or check [`curriculum_mapping.json`](curriculum_mapping.json):
     ```powershell
     python problem_manager.py "<problem or method name or date>"
     ```
   - This returns the exact month (`oct`, `nov`, `dec`), week (`week-1` to `week-5`), day folder (`01-oct` to `31-dec`), day number, and the required 3 problems for that day.

2. **Save the Solution File(s)**:
   - Target Folder: `<month>/<week>/<month-date>/` (all lowercase with hyphens, e.g., `oct/week-4/22-oct/`).
   - File Naming: `problem_{problem_number}_{snake_case_name}.py` (e.g., `problem_1_binary_search.py`).
   - Ensure the solution strictly follows the **No-Libraries Rule** (built from primitives; no `Counter`, `deque`, `bisect`, `heapq`, `itertools`, etc.).

3. **Generate or Update the Daily `README.md`**:
   In that specific day folder (`<month>/<week>/<month-date>/README.md`), ensure the following required sections are present:
   - **Header**: `# Day {day_num} · {month-date} ({day_of_week})`
   - **Topic**: Topic name from `curriculum_mapping.json`
   - **DON'T REACH FOR**: The forbidden library/shortcut rule for that day
   - **Per-Problem Breakdown**:
     - Problem name & clickable link to the `.py` file
     - **Approach** (2–3 lines)
     - **Time Complexity** (e.g. `O(log N)` or `O(N)`)
     - **Space Complexity** (e.g. `O(1)`)
     - **Edge Case Missed on First Attempt**
   - **Discord Submission Command**:
     ```text
     /done day{day_num} <link_to_prob_1> <link_to_prob_2> <link_to_prob_3>
     ```
     Using the repo base URL: `https://github.com/gameway-sn/DSA_ALPHA_300/blob/main/<relative-path-to-py>`

4. **Git Commit & Push**:
   Run the following terminal commands:
   ```powershell
   git add .
   git commit -m "Add Day {N} ({date}): {Topic/Problem Names} solutions and README"
   git push origin main
   ```

5. **Respond to the User**:
   - Confirm the files created and target folder.
   - Provide the clickable GitHub links to the pushed files.
   - Print the exact Discord `/done` command ready to copy and paste.

---

## 🛠️ Repository Specifications

- **Git Remote**: `https://github.com/gameway-sn/DSA_ALPHA_300.git`
- **Default Branch**: `main`
- **Mapping Source of Truth**: [`curriculum_mapping.json`](curriculum_mapping.json)
- **Helper Script**: [`problem_manager.py`](problem_manager.py)
