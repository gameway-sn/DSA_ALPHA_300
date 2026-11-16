# Day 16 · 16-nov (Mon)

**Topic**: Sliding window on strings (echo of Oct Days 11-14)  
**DON'T REACH FOR**: `Counter inside loop. Maintain window freq dict incrementally.`

---

## 📝 Problems & Solutions

### Problem 1: Longest Substring Without Repeating Characters
- **Solution File**: [`problem_1_longest_substring_without_repeating_characters.py`](./problem_1_longest_substring_without_repeating_characters.py)
- **Approach**:
  Maintain a dynamic sliding window `[i, j]` tracked by a character hash set `w`. Advance the right pointer `j`; if `s[j]` is already present in `w`, shrink from the left by removing `s[i]` and advancing `i`. Otherwise, add `s[j]` to `w`, update the maximum length `r = max(len(w), r)`, and advance `j`.
- **Time Complexity**: `O(N)` where `N` is the length of `s` (each character is visited by `i` and `j` at most once).
- **Space Complexity**: `O(K)` where `K` is the size of the unique character set (`\min(N, |\Sigma|)`).
- **Edge Case Missed on First Attempt**:
  Empty string `s = ""` returning `0`, and strings consisting of all identical characters (e.g., `"bbbbb"`) maintaining a maximum window of `1`.

---

## 💬 Discord Submission Command
```text
/done day16 https://github.com/gameway-sn/DSA_ALPHA_300/blob/main/nov/week-3/16-nov/problem_1_longest_substring_without_repeating_characters.py https://github.com/gameway-sn/DSA_ALPHA_300/blob/main/nov/week-3/16-nov/problem_2_longest_repeating_character_replacement.py https://github.com/gameway-sn/DSA_ALPHA_300/blob/main/nov/week-3/16-nov/problem_3_find_all_anagrams_in_a_string.py
```
