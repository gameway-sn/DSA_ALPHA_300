# Day 5 · 05-oct (Mon)

**Topic**: Set membership + missing  
**DON'T REACH FOR**: `set operations (& | -). Walk the arrays manually.`

---

## 📝 Problems & Solutions

### Problem 1: Intersection of Two Arrays
- **Solution File**: [`problem_1_intersection_of_two_arrays.py`](./problem_1_intersection_of_two_arrays.py)
- **Approach**:
  Deduplicate both input arrays into hash sets `num1` and `num2` for $O(1)$ membership checks. Repeatedly pop elements from `num2` and check membership in `num1`; upon match, append to result `r` and remove from `num1` to prevent duplicates without using built-in set intersection operators (`&`).
- **Time Complexity**: `O(N + M)` where `N = len(nums1)` and `M = len(nums2)`.
- **Space Complexity**: `O(N + M)` to hold the sets for `nums1` and `nums2`.
- **Edge Case Missed on First Attempt**:
  Inputs containing duplicate numbers (e.g., `nums1 = [4, 9, 5]`, `nums2 = [9, 4, 9, 8, 4]`), which are deduplicated by the set construction and removal on hit.

---

## 💬 Discord Submission Command
```text
/done day5 https://github.com/gameway-sn/DSA_ALPHA_300/blob/main/oct/week-1/05-oct/problem_1_intersection_of_two_arrays.py https://github.com/gameway-sn/DSA_ALPHA_300/blob/main/oct/week-1/05-oct/problem_2_missing_number.py https://github.com/gameway-sn/DSA_ALPHA_300/blob/main/oct/week-1/05-oct/problem_3_find_all_numbers_disappeared_in_an_array.py
```

