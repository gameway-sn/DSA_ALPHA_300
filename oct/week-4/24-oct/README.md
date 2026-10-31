# Day 24 · 24-oct (Sat)

**Topic**: Binary search variants (first + last occurrence)  
**DON'T REACH FOR**: `bisect_left, bisect_right. Build both variants yourself.`

---

## 📝 Problems & Solutions

### Problem 1: Find First and Last Position in Sorted Array
- **Solution File**: [`problem_1_find_first_and_last_position_in_sorted_array.py`](./problem_1_find_first_and_last_position_in_sorted_array.py)
- **Approach**:
  Locate any occurrence of `target` using standard binary search. Once found at index `m`, initiate two targeted binary searches: search `[0, m]` adjusting `h1 = m1 - 1` to find the earliest (first) position, and search `[m, len(nums) - 1]` adjusting `l2 = m2 + 1` to find the latest (last) position.
- **Time Complexity**: `O(log N)`
- **Space Complexity**: `O(1)`
- **Edge Case Missed on First Attempt**:
  Empty array `nums = []` or target not present returning `[-1, -1]`, and arrays where all elements are identical to the target (e.g. `[8, 8, 8, 8]` correctly spanning `[0, 3]`).

---

## 💬 Discord Submission Command
```text
/done day24 https://github.com/gameway-sn/DSA_ALPHA_300/blob/main/oct/week-4/24-oct/problem_1_find_first_and_last_position_in_sorted_array.py https://github.com/gameway-sn/DSA_ALPHA_300/blob/main/oct/week-4/24-oct/problem_2_count_occurrences_of_element_in_sorted_array.py https://github.com/gameway-sn/DSA_ALPHA_300/blob/main/oct/week-4/24-oct/problem_3_floor_and_ceiling_in_sorted_array.py
```
