# Day 1 · 01-oct (Thu)

**Topic**: Array traversal + hashmap lookup  
**DON'T REACH FOR**: `Counter, list(set(...)). Build the dict yourself with one pass.`

---

## 📝 Problems & Solutions

### Problem 1: Two Sum
- **Solution File**: [`problem_1_two_sum.py`](./problem_1_two_sum.py)
- **Approach**:
  Use a single-pass hash map to record seen numbers and their indices. For each element, calculate its complement (`target - i`) and check if it already exists in the map; if so, return the matching pair of indices.
- **Time Complexity**: `O(N)`
- **Space Complexity**: `O(N)`
- **Edge Case Missed on First Attempt**:
  Using the same element twice (prevented by looking up complement before adding current element) and handling duplicate values that sum up to target.

---

### Problem 2: Contains Duplicate
- **Solution File**: [`problem_2_contains_duplicate.py`](./problem_2_contains_duplicate.py)
- **Approach**:
  Build a frequency hash map by iterating over the array and counting occurrences of each element without using `collections.Counter`. Iterate through the frequency values and return `True` if any count exceeds 1, else `False`.
- **Time Complexity**: `O(N)`
- **Space Complexity**: `O(N)`
- **Edge Case Missed on First Attempt**:
  Single-element arrays (e.g. `[1]`), where no duplicates can exist, and negative numbers as keys.

---

### Problem 3: Single Number
- **Solution File**: [`problem_3_single_number.py`](./problem_3_single_number.py)
- **Approach**:
  Leverage XOR bitwise logic where `x ^ x = 0` and `x ^ 0 = x`. Iteratively XOR all elements together; duplicates cancel each other out, leaving only the unique element with `O(1)` auxiliary memory.
- **Time Complexity**: `O(N)`
- **Space Complexity**: `O(1)`
- **Edge Case Missed on First Attempt**:
  Single-element arrays `nums = [1]` where the loop runs once and returns `1`, and negative integers handled naturally by two's complement bitwise XOR.

---

## 💬 Discord Submission Command
```text
/done day1 https://github.com/gameway-sn/DSA_ALPHA_300/blob/main/oct/week-1/01-oct/problem_1_two_sum.py https://github.com/gameway-sn/DSA_ALPHA_300/blob/main/oct/week-1/01-oct/problem_2_contains_duplicate.py https://github.com/gameway-sn/DSA_ALPHA_300/blob/main/oct/week-1/01-oct/problem_3_single_number.py
```


