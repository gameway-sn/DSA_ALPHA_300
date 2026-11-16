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

### Problem 2: Longest Repeating Character Replacement
- **Solution File**: [`problem_2_longest_repeating_character_replacement.py`](./problem_2_longest_repeating_character_replacement.py)
- **Approach**:
  Sliding window maintaining character frequency counts in dictionary `h` and the highest single character frequency `m`. When the number of required replacements `(window_len - m)` exceeds `k`, decrement `h[s[i]]` and advance left pointer `i`. Otherwise, expand window at `j`, updating `m` and recording max window span `r`.
- **Time Complexity**: `O(N)` where `N` is `len(s)`.
- **Space Complexity**: `O(K)` auxiliary space (at most 26 uppercase English letters).
- **Edge Case Missed on First Attempt**:
  Calculating window length as `abs(i - j)` rather than `(j - i + 1)`, causing off-by-one window measurements and failing to record the final valid expansion on the trailing index.

---

## 💬 Discord Submission Command
```text
/done day16 https://github.com/gameway-sn/DSA_ALPHA_300/blob/main/nov/week-3/16-nov/problem_1_longest_substring_without_repeating_characters.py https://github.com/gameway-sn/DSA_ALPHA_300/blob/main/nov/week-3/16-nov/problem_2_longest_repeating_character_replacement.py https://github.com/gameway-sn/DSA_ALPHA_300/blob/main/nov/week-3/16-nov/problem_3_find_all_anagrams_in_a_string.py
```
