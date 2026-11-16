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

#### Alternative Solution (v2)
- **Solution File**: [`problem_2_longest_repeating_character_replacement_v2.py`](./problem_2_longest_repeating_character_replacement_v2.py)
- **Approach**:
  Corrected sliding window with exact window span `(j - i + 1)`. Dynamically track character frequencies in hash map `h` and the maximum frequency `m`. Shrink window from the left while `(j - i + 1) - m > k`, maintaining optimal valid windows at each step.
- **Time Complexity**: `O(N)` where `N` is `len(s)` (each character pushed and popped at most once).
- **Space Complexity**: `O(1)` auxiliary space (bounded by 26 English uppercase characters).
- **Edge Case Missed on First Attempt**:
  Accurately measures window span with `j - i + 1` and properly evaluates the final index expansion.

---

### Problem 3: Find All Anagrams in a String
- **Solution File**: [`problem_3_find_all_anagrams_in_a_string.py`](./problem_3_find_all_anagrams_in_a_string.py)
- **Approach**:
  Build a frequency dict `forgoal` for pattern `p`. Slide a fixed window of size `n = len(p)` over `s` using `left` and `right` pointers, maintaining `forstring` incrementally — add `s[right]` on expansion, remove `s[left]` (deleting the key when it hits 0) when window exceeds `n`. Compare dicts each step; append `left` to result when equal.
- **Time Complexity**: `O(N)` where `N = len(s)` — each character visited once; dict comparison is `O(1)` (bounded 26-char alphabet).
- **Space Complexity**: `O(1)` auxiliary space (at most 26 lowercase English letters in each dict).
- **Edge Case Missed on First Attempt**:
  Deleting keys with zero count from `forstring` before comparing — without deletion, `forstring == forgoal` would fail even when frequencies match (extra zero-valued keys cause inequality).

---

## 💬 Discord Submission Command
```text
/done day16 https://github.com/gameway-sn/DSA_ALPHA_300/blob/main/nov/week-3/16-nov/problem_1_longest_substring_without_repeating_characters.py https://github.com/gameway-sn/DSA_ALPHA_300/blob/main/nov/week-3/16-nov/problem_2_longest_repeating_character_replacement.py https://github.com/gameway-sn/DSA_ALPHA_300/blob/main/nov/week-3/16-nov/problem_3_find_all_anagrams_in_a_string.py
```
