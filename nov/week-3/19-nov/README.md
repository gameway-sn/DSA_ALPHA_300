# Day 19 · 19-nov (Thu)

**Topic**: Binary search on strings (echo of Oct Week 4)  
**DON'T REACH FOR**: `bisect. Use your own BS from Oct Day 22.`

---

## 📝 Problems & Solutions

### Problem 1: Find Smallest Letter Greater Than Target
- **Solution File**: [`problem_1_find_smallest_letter_greater_than_target.py`](./problem_1_find_smallest_letter_greater_than_target.py)
- **Approach**:
  Custom binary search narrows `[l, h]` down to a window of at most two letters (`l < h - 1`), moving `l` past a match when `letters[m] == target`. Then scan that tiny window for the smallest letter strictly greater than the target. If none is greater, wrap around and return `letters[0]`.
- **Time Complexity**: `O(log N)` where `N = len(letters)`.
- **Space Complexity**: `O(1)`.
- **Edge Case Missed on First Attempt**:
  None recorded. Wrap-around (target >= last letter) is handled by the `'}'` sentinel fallback to `letters[0]`, and duplicates of the target are skipped via `l = m + 1`.

---

### Problem 2: Longest Word in Dictionary Through Deleting
- **Solution File**: [`problem_2_longest_word_in_dictionary_through_deleting.py`](./problem_2_longest_word_in_dictionary_through_deleting.py)
- **Approach**:
  Build a character-frequency hash map for `s`. For each dictionary word, build its own frequency map and check that `s` has at least that many of every character. Among valid words keep the longest, breaking ties by the lexicographically smaller word. No built-in sort or library is used.
- **Time Complexity**: `O(|s| + sum of word lengths)`.
- **Space Complexity**: `O(1)` (maps bounded by the alphabet size).
- **Edge Case Missed on First Attempt**:
  The frequency check ignores character order, so it accepts words that are not subsequences of `s` (e.g. `s = "ba"`, word `"ab"`). A two-pointer subsequence check per word is the correct validity test.

---

### Problem 3: Lexicographically Smallest Equivalent String
> Note: the curriculum lists "Lexicographic Smaller String Comparison" for this slot; the submitted solution is for this problem instead.

- **Solution File**: [`problem_3_lexicographically_smallest_equivalent_string.py`](./problem_3_lexicographically_smallest_equivalent_string.py)
- **Approach**:
  Union-Find over the 26 letters. For each pair `(s1[i], s2[i])`, union their sets, always making the smaller letter the root so the root is the lexicographically smallest member. Then map each character of `baseStr` to its root. Path compression is used in `find`. No libraries are used.
- **Time Complexity**: `O((N + M) * alpha(26))`, effectively `O(N + M)` where `N = len(s1)` and `M = len(baseStr)`.
- **Space Complexity**: `O(1)` for the 26-element parent array (plus `O(M)` for the result).
- **Edge Case Missed on First Attempt**:
  None recorded. Unioning by the smaller root keeps the smallest letter as representative, and letters in `baseStr` not in any pair map to themselves.

---

## 💬 Discord Submission Command
```text
/done day19 https://github.com/gameway-sn/DSA_ALPHA_300/blob/main/nov/week-3/19-nov/problem_1_find_smallest_letter_greater_than_target.py https://github.com/gameway-sn/DSA_ALPHA_300/blob/main/nov/week-3/19-nov/problem_2_longest_word_in_dictionary_through_deleting.py https://github.com/gameway-sn/DSA_ALPHA_300/blob/main/nov/week-3/19-nov/problem_3_lexicographically_smallest_equivalent_string.py
```
