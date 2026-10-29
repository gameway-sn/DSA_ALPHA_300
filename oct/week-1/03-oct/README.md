# Day 3 · 03-oct (Sat)

**Topic**: Hashmap counting  
**DON'T REACH FOR**: `Counter, Counter.most_common(). Use a plain dict with manual increment.`

---

## 📝 Problems & Solutions

### Problem 1: Majority Element
- **Solution File**: [`problem_1_majority_element.py`](./problem_1_majority_element.py)
- **Approach**:
  Implemented Boyer-Moore Voting Algorithm maintaining a candidate `res` and a running counter `count`. Whenever `count` drops to `0`, a new candidate is chosen. Matching elements increment `count` and differing elements decrement `count`, isolating the majority element in optimal space without library counters.
- **Time Complexity**: `O(N)`
- **Space Complexity**: `O(1)`
- **Edge Case Missed on First Attempt**:
  Single-element arrays `nums = [1]` returning immediately with `count = 1`, and alternating sequences where the majority element appears predominantly in the second half.

---

## 💬 Discord Submission Command
```text
/done day3 https://github.com/gameway-sn/DSA_ALPHA_300/blob/main/oct/week-1/03-oct/problem_1_majority_element.py https://github.com/gameway-sn/DSA_ALPHA_300/blob/main/oct/week-1/03-oct/problem_2_first_non_repeating_element_in_array.py https://github.com/gameway-sn/DSA_ALPHA_300/blob/main/oct/week-1/03-oct/problem_3_count_frequencies_of_array_elements.py
```
