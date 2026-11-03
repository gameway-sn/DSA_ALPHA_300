# Day 1 · 01-nov (Sun)

**Topic**: Length, concat, basic string ops  
**DON'T REACH FOR**: `len() on dynamically built string in a loop (O(n²) with +=). Build via list, join at end.`

---

## 📝 Problems & Solutions

### Problem 1: Length of Last Word
- **Solution File**: [`problem_1_length_of_last_word.py`](./problem_1_length_of_last_word.py)
- **Approach**:
  Split the input string `s` across whitespace into words using `split()`. Retrieve the last word at index `-1` and return its length using `len()`.
- **Time Complexity**: `O(N)`
- **Space Complexity**: `O(N)`
- **Edge Case Missed on First Attempt**:
  Strings with trailing whitespace or variable gaps between words (e.g. `"   fly me   to   the moon  "`), which whitespace-splitting cleans up automatically.

---

## 💬 Discord Submission Command
```text
/done day1 https://github.com/gameway-sn/DSA_ALPHA_300/blob/main/nov/week-1/01-nov/problem_1_length_of_last_word.py https://github.com/gameway-sn/DSA_ALPHA_300/blob/main/nov/week-1/01-nov/problem_2_longest_common_prefix.py https://github.com/gameway-sn/DSA_ALPHA_300/blob/main/nov/week-1/01-nov/problem_3_count_and_say.py
```
