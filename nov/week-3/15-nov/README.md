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

### Problem 2: Repeated Substring Pattern
- **Solution File**: [`problem_2_repeated_substring_pattern.py`](./problem_2_repeated_substring_pattern.py)
- **Approach**:
  Concatenate `s` with itself to form `s + s` and strip the outermost boundaries `[1:-1]`. Check if `s` exists in the trimmed string; if `s` is periodic with a repeating unit, the periodic alignment guarantees `s` appears within the trimmed interior.
- **Time Complexity**: `O(N)` where `N` is the length of `s`.
- **Space Complexity**: `O(N)` to construct the doubled and sliced string.
- **Edge Case Missed on First Attempt**:
  Omitting the `[1:-1]` slice trimming causes any string to trivially match at index $0$ or index $N$.

---

## 💬 Discord Submission Command
```text
/done day15 https://github.com/gameway-sn/DSA_ALPHA_300/blob/main/nov/week-3/15-nov/problem_1_find_the_index_of_the_first_occurrence_strstr.py https://github.com/gameway-sn/DSA_ALPHA_300/blob/main/nov/week-3/15-nov/problem_2_repeated_substring_pattern.py https://github.com/gameway-sn/DSA_ALPHA_300/blob/main/nov/week-3/15-nov/problem_3_rotate_string_via_substring_match.py
```
