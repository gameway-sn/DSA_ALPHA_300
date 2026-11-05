# Day 8 · 08-oct (Thu)

**Topic**: Two pointers from ends  
**DON'T REACH FOR**: `s == s[::-1]. Write the two-pointer walk.`

---

## 📝 Problems & Solutions

### Problem 1: Valid Palindrome
- **Solution File**: [`problem_1_valid_palindrome.py`](./problem_1_valid_palindrome.py)
- **Approach**:
  Use two pointers `i` and `j` starting at opposite ends of string `s`. Advance inward while skipping non-alphanumeric characters using `.isalnum()`. Compare valid characters in lowercase; if unequal, return `False`. If the pointers cross without conflict, return `True`.
- **Time Complexity**: `O(N)` where `N` is `len(s)`.
- **Space Complexity**: `O(1)` auxiliary space without generating reversed string copies.
- **Edge Case Missed on First Attempt**:
  Strings with only non-alphanumeric characters (e.g. `" "`, `".,"`), where pointers cross without character comparisons and correctly evaluate to `True`.

---

## 💬 Discord Submission Command
```text
/done day8 https://github.com/gameway-sn/DSA_ALPHA_300/blob/main/oct/week-2/08-oct/problem_1_valid_palindrome.py https://github.com/gameway-sn/DSA_ALPHA_300/blob/main/oct/week-2/08-oct/problem_2_reverse_string.py https://github.com/gameway-sn/DSA_ALPHA_300/blob/main/oct/week-2/08-oct/problem_3_reverse_vowels_of_a_string.py
```

