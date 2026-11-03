# Day 3 · 03-nov (Tue)

**Topic**: Character frequency counting (dict pattern)  
**DON'T REACH FOR**: `Counter, Counter.most_common(). Build the dict manually.`

---

## 📝 Problems & Solutions

### Problem 1: Valid Anagram
- **Solution File**: [`problem_1_valid_anagram.py`](./problem_1_valid_anagram.py)
- **Approach**:
  First verify length equality between `s` and `t` (return `False` if lengths differ). Iterate through indices and populate frequency counts for both strings into standard Python dictionaries using `.get(key, 0)` without importing `Counter`. Check equality of the two frequency maps.
- **Time Complexity**: `O(N)` where `N` is the length of `s`.
- **Space Complexity**: `O(1)` auxiliary space (bounded by character set size $\le 26$).
- **Edge Case Missed on First Attempt**:
  Unequal string lengths (e.g. `s = "a"`, `t = "ab"`), and single-character mismatch strings.

---

## 💬 Discord Submission Command
```text
/done day3 https://github.com/gameway-sn/DSA_ALPHA_300/blob/main/nov/week-1/03-nov/problem_1_valid_anagram.py https://github.com/gameway-sn/DSA_ALPHA_300/blob/main/nov/week-1/03-nov/problem_2_group_anagrams.py https://github.com/gameway-sn/DSA_ALPHA_300/blob/main/nov/week-1/03-nov/problem_3_first_unique_character_in_a_string.py
```
