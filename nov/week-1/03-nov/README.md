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

### Problem 2: Group Anagrams
- **Solution File**: [`problem_2_group_anagrams.py`](./problem_2_group_anagrams.py)
- **Approach**:
  Represent each string's character distribution with an immutable 26-element tuple derived from `ord(c) - 97` counts. Use this tuple as the hash map key to group the original indices of anagram words, and finally build the list of grouped string buckets.
- **Time Complexity**: `O(N \cdot K)` where `N` is the number of strings and `K` is the maximum length of a string.
- **Space Complexity**: `O(N \cdot K)` to store hash map buckets and output groups.
- **Edge Case Missed on First Attempt**:
  Empty strings `strs = [""]` yielding the zero tuple `(0, 0, ..., 0)` and single-character strings grouped accurately without key collisions.

---

### Problem 3: First Unique Character in a String
- **Solution File**: [`problem_3_first_unique_character_in_a_string.py`](./problem_3_first_unique_character_in_a_string.py)
- **Approach**:
  Scan through `s` tracking character indices in dictionary `hm`. If character `c` is already in `hm`, pop it; otherwise record its first seen index. Find and return the minimum index remaining in `hm`, or `-1` if all characters had duplicates.
- **Time Complexity**: `O(N)` where `N` is the length of `s`.
- **Space Complexity**: `O(1)` auxiliary space (at most 26 lowercase English letters).
- **Edge Case Missed on First Attempt**:
  Characters appearing 3 or more times (e.g. `"aaa"`, where alternating pop/insert cycles can inadvertently re-insert a previously seen character). A separate frequency map or tombstone/seen set ensures characters seen $\ge 2$ times are permanently flagged.

---

## 💬 Discord Submission Command
```text
/done day3 https://github.com/gameway-sn/DSA_ALPHA_300/blob/main/nov/week-1/03-nov/problem_1_valid_anagram.py https://github.com/gameway-sn/DSA_ALPHA_300/blob/main/nov/week-1/03-nov/problem_2_group_anagrams.py https://github.com/gameway-sn/DSA_ALPHA_300/blob/main/nov/week-1/03-nov/problem_3_first_unique_character_in_a_string.py
```
