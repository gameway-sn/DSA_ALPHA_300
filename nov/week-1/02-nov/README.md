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

### Problem 2: Capitalize the Title
- **Solution File**: [`problem_2_capitalize_the_title.py`](./problem_2_capitalize_the_title.py)
- **Approach**:
  Split `title` into words. For words of length $\le 2$, convert every character to lowercase using manual ASCII offset (`chr(cv + 32)` for `65 <= cv <= 90`). For words of length $> 2$, capitalize the initial character (`chr(cv - 32)` for `97 <= cv <= 122`) and lowercase the remaining characters. Join words with single spaces.
- **Time Complexity**: `O(N)` where `N` is the length of `title`.
- **Space Complexity**: `O(N)`
- **Edge Case Missed on First Attempt**:
  Words with 1 or 2 characters that start uppercase (e.g., `"OF"`, `"A"`, `"iN"`), which must be converted entirely to lowercase rather than capitalized.

---

### Problem 3: Defanging an IP Address
- **Solution File**: [`problem_3_defanging_an_ip_address.py`](./problem_3_defanging_an_ip_address.py)
- **Approach**:
  Iterate over each character `c` of the IP string. Replace every occurrence of `.` with `[.]` by appending to an accumulator list, keeping octet digit characters unchanged, and join the result.
- **Time Complexity**: `O(N)` where `N` is the length of the string.
- **Space Complexity**: `O(N)`
- **Edge Case Missed on First Attempt**:
  Addresses with single-digit octets (e.g. `"0.0.0.0"`) or maximum length octets (`"255.255.255.255"`), handled consistently without string concatenation in a loop.

---

## 💬 Discord Submission Command
```text
/done day2 https://github.com/gameway-sn/DSA_ALPHA_300/blob/main/nov/week-1/02-nov/problem_1_to_lower_case.py https://github.com/gameway-sn/DSA_ALPHA_300/blob/main/nov/week-1/02-nov/problem_2_capitalize_the_title.py https://github.com/gameway-sn/DSA_ALPHA_300/blob/main/nov/week-1/02-nov/problem_3_defanging_an_ip_address.py
```
