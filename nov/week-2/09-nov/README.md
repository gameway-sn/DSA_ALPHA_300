# Day 9 · 09-nov (Mon)

**Topic**: Reverse by chunks / per-word  
**DON'T REACH FOR**: `list comprehension with [::-1]. Build character-by-character.`

---

## 📝 Problems & Solutions

### Problem 1: Reverse Words in a String III
- **Solution File**: [`problem_1_reverse_words_in_a_string_iii.py`](./problem_1_reverse_words_in_a_string_iii.py)
- **Approach**:
  Split the input string `s` into words with `.split()`. Iterate through words in forward order, reversing each individual word `w` using helper `rev` (`w[::-1]`), and join the reversed words with single whitespace.
- **Time Complexity**: `O(N)` where `N` is the length of `s`.
- **Space Complexity**: `O(N)` for word tokens and reversed strings.
- **Edge Case Missed on First Attempt**:
  Single-word strings without spaces (e.g., `"Word"` -> `"droW"`), and ensuring original word ordering is maintained while reversing each word's characters.

---

### Problem 2: Reverse Prefix of Word
- **Solution File**: [`problem_2_reverse_prefix_of_word.py`](./problem_2_reverse_prefix_of_word.py)
- **Approach**:
  Locate the first occurrence of `ch` in `word`. Reverse the prefix slice up to and including that index (`word[:loc+1]`) using helper `rev` (`[::-1]`), concatenate the remaining suffix `word[loc+1:]`, and return the full word if `ch` is absent.
- **Time Complexity**: `O(N)` where `N` is the length of `word`.
- **Space Complexity**: `O(N)` for string slices.
- **Edge Case Missed on First Attempt**:
  Character `ch` not found in `word` (leaving string unchanged), or `ch` located at index 0 where the single-character prefix mirrors into itself.

---

## 💬 Discord Submission Command
```text
/done day9 https://github.com/gameway-sn/DSA_ALPHA_300/blob/main/nov/week-2/09-nov/problem_1_reverse_words_in_a_string_iii.py https://github.com/gameway-sn/DSA_ALPHA_300/blob/main/nov/week-2/09-nov/problem_2_reverse_prefix_of_word.py https://github.com/gameway-sn/DSA_ALPHA_300/blob/main/nov/week-2/09-nov/problem_3_reverse_vowels_of_a_string.py
```
