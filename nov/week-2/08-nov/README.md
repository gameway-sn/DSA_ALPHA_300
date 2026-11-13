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

### Problem 2: Reverse String II
- **Solution File**: [`problem_2_reverse_string_ii.py`](./problem_2_reverse_string_ii.py)
- **Approach**:
  Process the string in steps of $2k$. In each step, reverse the first $k$ characters (`s[i:i+k]`) via helper `rev` and keep the subsequent $k$ characters (`s[i+k:i+2*k]`) intact. Join the accumulated chunks into the final string.
- **Time Complexity**: `O(N)` where `N` is `len(s)`.
- **Space Complexity**: `O(N)` to hold segment slices and final string.
- **Edge Case Missed on First Attempt**:
  Tail segments with fewer than $k$ characters remaining (which must be reversed in their entirety) or between $k$ and $2k$ characters remaining, naturally satisfied by slice boundary clipping.

---

### Problem 3: Reverse Only Letters
- **Solution File**: [`problem_3_reverse_only_letters.py`](./problem_3_reverse_only_letters.py)
- **Approach**:
  Decompose string `s` into character list `r`. Use a two-pointer walk (`rev2`) starting from both ends `i = 0` and `j = len(l) - 1`. Non-alphabetic characters remain fixed in their original indices, while two pointers advance inward until both encounter alphabetic characters (`c.isalpha()`), swapping their positions before returning the joined string.
- **Time Complexity**: `O(N)` where `N` is `len(s)`.
- **Space Complexity**: `O(N)` for list manipulation and character arrays.
- **Edge Case Missed on First Attempt**:
  Strings without any letters (e.g. `"!@#$-_"` remaining unchanged) or with letters interspersed with complex symbols and dashes (`"a-bC-dEf-ghIj"`).

---

## 💬 Discord Submission Command
```text
/done day8 https://github.com/gameway-sn/DSA_ALPHA_300/blob/main/nov/week-2/08-nov/problem_1_reverse_words_in_a_string.py https://github.com/gameway-sn/DSA_ALPHA_300/blob/main/nov/week-2/08-nov/problem_2_reverse_string_ii.py https://github.com/gameway-sn/DSA_ALPHA_300/blob/main/nov/week-2/08-nov/problem_3_reverse_only_letters.py
```
