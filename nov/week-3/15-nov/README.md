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

---

## 💬 Discord Submission Command
```text
/done day15 https://github.com/gameway-sn/DSA_ALPHA_300/blob/main/nov/week-3/15-nov/problem_1_find_the_index_of_the_first_occurrence_strstr.py https://github.com/gameway-sn/DSA_ALPHA_300/blob/main/nov/week-3/15-nov/problem_2_repeated_substring_pattern.py https://github.com/gameway-sn/DSA_ALPHA_300/blob/main/nov/week-3/15-nov/problem_3_rotate_string_via_substring_match.py
```
