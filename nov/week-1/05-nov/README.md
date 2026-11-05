# Day 5 · 05-nov (Thu)

**Topic**: Palindromes — two pointers from ends (echo of Oct Day 8)  
**DON'T REACH FOR**: `s == s[::-1]. Two-pointer walk.`

---

## 📝 Problems & Solutions

### Problem 2: Palindrome Number
- **Solution File**: [`problem_2_palindrome_number.py`](./problem_2_palindrome_number.py)
- **Approach**:
  Immediately return `False` for negative integers since the negative sign cannot be mirrored. Reverse the positive integer mathematically using modulo (`% 10`) and integer division (`// 10`) without string casting or string slicing (`[::-1]`), then check if the reversed value equals the original integer.
- **Time Complexity**: `O(\log_{10} N)` where $N$ is the input integer (proportional to the number of digits).
- **Space Complexity**: `O(1)` auxiliary space.
- **Edge Case Missed on First Attempt**:
  Negative numbers (e.g. `-121` returning `False`), and non-zero numbers ending in zero (e.g. `10` where reversed value `1 != 10`).

---

### Problem 3: Count Palindromic Substrings
- **Solution File**: [`problem_3_count_palindromic_substrings.py`](./problem_3_count_palindromic_substrings.py)
- **Approach**:
  Expand around each potential palindrome center using two pointers. For each index `i`, check odd-length palindromes starting at `(i, i)` and even-length palindromes starting at `(i, i + 1)`. Expand outward while characters match, incrementing the palindrome count without slicing or string reversals.
- **Time Complexity**: `O(N^2)` where $N$ is the length of `s`.
- **Space Complexity**: `O(1)` auxiliary space.
- **Edge Case Missed on First Attempt**:
  Handling both odd-length and even-length palindrome centers (e.g. `"aa"` having an even center between adjacent letters).

---

## 💬 Discord Submission Command
```text
/done day5 https://github.com/gameway-sn/DSA_ALPHA_300/blob/main/nov/week-1/05-nov/problem_1_valid_palindrome.py https://github.com/gameway-sn/DSA_ALPHA_300/blob/main/nov/week-1/05-nov/problem_2_palindrome_number.py https://github.com/gameway-sn/DSA_ALPHA_300/blob/main/nov/week-1/05-nov/problem_3_count_palindromic_substrings.py
```
