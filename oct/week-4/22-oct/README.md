# Day 22 · 22-oct (Thu)

**Topic**: Classic binary search  
**DON'T REACH FOR**: `bisect, bisect_left, bisect_right. Write lo + (hi-lo)//2 by hand.`

---

## 📝 Problems & Solutions

### Problem 1: Binary Search
- **Solution File**: [`problem_1_binary_search.py`](./problem_1_binary_search.py)
- **Approach**:
  Maintain two boundary pointers `l = 0` and `h = len(nums) - 1`. Compute mid without built-in helpers, inspect `nums[m]`, and bisect the search space by shifting either `l = m + 1` or `h = m - 1` until the target is found or search space is exhausted.
- **Time Complexity**: `O(log N)`
- **Space Complexity**: `O(1)`
- **Edge Case Missed on First Attempt**:
  Single-element arrays `nums = [5]` with `target = 5` (found immediately) or `target = 2` (loop terminates and returns `-1`).

---

### Problem 2: Search Insert Position
- **Solution File**: [`problem_2_search_insert_position.py`](./problem_2_search_insert_position.py)
- **Approach**:
  Apply binary search over the sorted array. If target equals `nums[m]`, return `m`. When search boundaries cross (`l > h`), pointer `l` naturally points to the correct insertion rank index for target.
- **Time Complexity**: `O(log N)`
- **Space Complexity**: `O(1)`
- **Edge Case Missed on First Attempt**:
  Target strictly smaller than the first element (returns `0`) or strictly greater than the last element (returns `len(nums)`).

---

### Problem 3: First Bad Version
- **Solution File**: [`problem_3_first_bad_version.py`](./problem_3_first_bad_version.py)
- **Approach**:
  Binary search on the version range `[1, n]`. If version `m` is bad, the earliest failure lies in `[l, m]` so set `h = m`; if good, it lies strictly in `[m + 1, h]` so set `l = m + 1`. Loop terminates when `l == h`.
- **Time Complexity**: `O(log N)`
- **Space Complexity**: `O(1)`
- **Edge Case Missed on First Attempt**:
  Setting `h = m - 1` instead of `h = m` when `m` is bad could skip the first bad version if `m` itself was the answer.

---

## 💬 Discord Submission Command
```text
/done day22 https://github.com/gameway-sn/DSA_ALPHA_300/blob/main/oct/week-4/22-oct/problem_1_binary_search.py https://github.com/gameway-sn/DSA_ALPHA_300/blob/main/oct/week-4/22-oct/problem_2_search_insert_position.py https://github.com/gameway-sn/DSA_ALPHA_300/blob/main/oct/week-4/22-oct/problem_3_first_bad_version.py
```
