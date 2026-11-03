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

### Problem 2: Longest Common Prefix
- **Solution File**: [`problem_2_longest_common_prefix.py`](./problem_2_longest_common_prefix.py)
- **Approach**:
  Use vertical character scanning with pointer `pl`. At each character index, verify that every string in `strs` has length greater than `pl` and matches the character `strs[0][pl]`. On the first mismatch or boundary exhaustion, return the prefix slice `strs[0][0:pl]`.
- **Time Complexity**: `O(S)` where `S` is the sum of characters in all strings.
- **Space Complexity**: `O(1)` auxiliary space.
- **Edge Case Missed on First Attempt**:
  Empty input list `strs = []`, strings starting with `""`, or varying string lengths where one string terminates before mismatches occur.

---

### Problem 3: Count and Say
- **Solution File**: [`problem_3_count_and_say.py`](./problem_3_count_and_say.py)
- **Approach**:
  Initialize sequence at `w = "1"`. Iteratively generate the next term up to `n` by scanning consecutive characters and aggregating run counts into list `r` using `str(ct) + e`. Join the list at the end of each iteration to avoid $O(N^2)$ repeated string concatenation.
- **Time Complexity**: $O(2^n)$ in worst-case string expansion (bounded by Conway's sequence growth).
- **Space Complexity**: $O(M)$ where $M$ is the length of the string at step $n$.
- **Edge Case Missed on First Attempt**:
  Flushing the final run (`str(ct) + e`) after the character scan loop completes, and correctly returning `"1"` when `n = 1`.

---

## 💬 Discord Submission Command
```text
/done day1 https://github.com/gameway-sn/DSA_ALPHA_300/blob/main/nov/week-1/01-nov/problem_1_length_of_last_word.py https://github.com/gameway-sn/DSA_ALPHA_300/blob/main/nov/week-1/01-nov/problem_2_longest_common_prefix.py https://github.com/gameway-sn/DSA_ALPHA_300/blob/main/nov/week-1/01-nov/problem_3_count_and_say.py
```
