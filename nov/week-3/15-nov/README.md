# Day 15 · 15-nov (Sun)

**Topic**: Pattern matching (naive strStr)  
**DON'T REACH FOR**: `s.find(), s.index(), re.search(). Write the nested-loop match.`

---

## 📝 Problems & Solutions

### Problem 1: Find the Index of the First Occurrence (strStr)
- **Solution File**: [`problem_1_find_the_index_of_the_first_occurrence_strstr.py`](./problem_1_find_the_index_of_the_first_occurrence_strstr.py)
- **Approach**:
  Slide a window of length `len(needle)` across `haystack` sequentially. At each offset `i`, compare the window slice `haystack[i : i + len(needle)]` with `needle` without calling built-in search methods (`.find()` or `.index()`). Return `i` on match, or `-1` if exhausted.
- **Time Complexity**: `O((N - M + 1) \cdot M)` where `N` is `len(haystack)` and `M` is `len(needle)`.
- **Space Complexity**: `O(M)` for window slicing.
- **Edge Case Missed on First Attempt**:
  `needle` longer than `haystack` (`len(needle) > len(haystack)`) returning `-1` immediately, or occurrences matching at the exact boundary end of `haystack`.

#### Alternative Solution (v2)
- **Solution File**: [`problem_1_find_the_index_of_the_first_occurrence_strstr_v2.py`](./problem_1_find_the_index_of_the_first_occurrence_strstr_v2.py)
- **Approach**:
  Direct linear sliding-window comparison with print logging. Evaluates slices of length `len(needle)` against `needle` while advancing index `i`.
- **Time Complexity**: `O((N - M + 1) \cdot M)` where `N` is `len(haystack)` and `M` is `len(needle)`.
- **Space Complexity**: `O(M)` for window slices.
- **Edge Case Missed on First Attempt**:
  Naive sliding-window comparison takes $O(N \cdot M)$ time in the worst case (e.g., `haystack = "aaaaaab"`, `needle = "aab"`). A Knuth-Morris-Pratt (KMP) prefix-function table achieves true optimal $O(N + M)$ time complexity.

---

## 💬 Discord Submission Command
```text
/done day15 https://github.com/gameway-sn/DSA_ALPHA_300/blob/main/nov/week-3/15-nov/problem_1_find_the_index_of_the_first_occurrence_strstr.py https://github.com/gameway-sn/DSA_ALPHA_300/blob/main/nov/week-3/15-nov/problem_2_repeated_substring_pattern.py https://github.com/gameway-sn/DSA_ALPHA_300/blob/main/nov/week-3/15-nov/problem_3_rotate_string_via_substring_match.py
```
