# Day 8 · 08-nov (Sun)

**Topic**: Reverse operations (echo of Oct arrays reversal)  
**DON'T REACH FOR**: `s[::-1], reversed(), s.split()[::-1].`

---

## 📝 Problems & Solutions

### Problem 1: Reverse Words in a String
- **Solution File**: [`problem_1_reverse_words_in_a_string.py`](./problem_1_reverse_words_in_a_string.py)
- **Approach**:
  Extract individual word tokens using `s.split()` to normalize multiple spaces and trim edges. Traverse backwards through the word array with a manual decrementing loop (`range(len(s) - 1, -1, -1)`) avoiding `[::-1]` or `reversed()`, and join the reversed words with single space separators.
- **Time Complexity**: `O(N)` where `N` is the length of `s`.
- **Space Complexity**: `O(N)` to store word tokens and result array.
- **Edge Case Missed on First Attempt**:
  Leading or trailing spaces and multiple spaces between words (e.g. `"  hello world  "` -> `"world hello"`).

---

## 💬 Discord Submission Command
```text
/done day8 https://github.com/gameway-sn/DSA_ALPHA_300/blob/main/nov/week-2/08-nov/problem_1_reverse_words_in_a_string.py https://github.com/gameway-sn/DSA_ALPHA_300/blob/main/nov/week-2/08-nov/problem_2_reverse_string_ii.py https://github.com/gameway-sn/DSA_ALPHA_300/blob/main/nov/week-2/08-nov/problem_3_reverse_only_letters.py
```
