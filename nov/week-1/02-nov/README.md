# Day 2 · 02-nov (Mon)

**Topic**: Character transformation  
**DON'T REACH FOR**: `s.lower(), s.upper(), s.swapcase(). Walk the chars and ord-shift by hand.`

---

## 📝 Problems & Solutions

### Problem 1: To Lower Case
- **Solution File**: [`problem_1_to_lower_case.py`](./problem_1_to_lower_case.py)
- **Approach**:
  Iterate through the characters of string `s` and inspect their ASCII integer code via `ord()`. For uppercase characters in the ASCII range `[65, 90]`, shift to lowercase by adding 32 (`chr(e + 32)`). Append all other characters directly and join the accumulated list.
- **Time Complexity**: `O(N)`
- **Space Complexity**: `O(N)`
- **Edge Case Missed on First Attempt**:
  Strings with non-alphabet characters (symbols, punctuation, digits, whitespace) and already-lowercase characters, which are preserved unchanged.

---

## 💬 Discord Submission Command
```text
/done day2 https://github.com/gameway-sn/DSA_ALPHA_300/blob/main/nov/week-1/02-nov/problem_1_to_lower_case.py https://github.com/gameway-sn/DSA_ALPHA_300/blob/main/nov/week-1/02-nov/problem_2_capitalize_the_title.py https://github.com/gameway-sn/DSA_ALPHA_300/blob/main/nov/week-1/02-nov/problem_3_defanging_an_ip_address.py
```
