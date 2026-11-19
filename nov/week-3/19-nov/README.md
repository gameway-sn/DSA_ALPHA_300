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

## 💬 Discord Submission Command
```text
/done day19 https://github.com/gameway-sn/DSA_ALPHA_300/blob/main/nov/week-3/19-nov/problem_1_find_smallest_letter_greater_than_target.py <link_to_prob_2> <link_to_prob_3>
```
