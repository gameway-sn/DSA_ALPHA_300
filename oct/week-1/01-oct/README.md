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

## 💬 Discord Submission Command
```text
/done day1 https://github.com/gameway-sn/DSA_ALPHA_300/blob/main/oct/week-1/01-oct/problem_1_two_sum.py https://github.com/gameway-sn/DSA_ALPHA_300/blob/main/oct/week-1/01-oct/problem_2_contains_duplicate.py https://github.com/gameway-sn/DSA_ALPHA_300/blob/main/oct/week-1/01-oct/problem_3_single_number.py
```
