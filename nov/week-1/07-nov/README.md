# Day 7 · 07-nov (Sat)

**Topic**: Character classification  
**DON'T REACH FOR**: `ch.isalpha(), ch.isdigit() for the LOGIC — fine for the check. str.translate shortcuts banned.`

---

## 📝 Problems & Solutions

### Problem 1: Check if the Sentence Is Pangram
- **Solution File**: [`problem_1_check_if_the_sentence_is_pangram.py`](./problem_1_check_if_the_sentence_is_pangram.py)
- **Approach**:
  Build a reference set containing all 26 lowercase English alphabet characters and convert the input string into a set of unique seen characters. Verify that the full alphabet set is a subset of the sentence set (`set_az.issubset(set(sentence))`).
- **Time Complexity**: `O(N)` where `N` is the length of `sentence`.
- **Space Complexity**: `O(1)` auxiliary space (at most 26 lowercase English letters).
- **Edge Case Missed on First Attempt**:
  Sentences shorter than 26 characters (which can never be pangrams) or sentences containing repeated letters that miss exactly one letter from the alphabet.

---

### Problem 2: Number of Segments in a String
- **Solution File**: [`problem_2_number_of_segments_in_a_string.py`](./problem_2_number_of_segments_in_a_string.py)
- **Approach**:
  Iterate through the string maintaining a slice start index `st`. On encountering whitespace delimiter `s[i] == " "`, slice the substring `s[st:i]` and advance `st = i + 1`.
- **Time Complexity**: `O(N)` where `N` is the length of string `s`.
- **Space Complexity**: `O(N)` to hold segment slices.
- **Edge Case Missed on First Attempt**:
  Consecutive whitespace creating empty slices `""`, omitting the final trailing word segment, and returning `r` directly rather than the non-empty segment count `len([w for w in r if w])` or transition count `(i == 0 or s[i-1] == ' ') and s[i] != ' '`.

#### Alternative Solution (v2)
- **Solution File**: [`problem_2_number_of_segments_in_a_string_v2.py`](./problem_2_number_of_segments_in_a_string_v2.py)
- **Approach**:
  Single-pass character scan using a boolean state flag `prev` to track whether the previous character was part of a segment. Increment the count `r` only upon entering a new non-whitespace segment (`c != " " and not prev`), and reset `prev = False` whenever a space is met.
- **Time Complexity**: `O(N)` where `N` is the length of `s`.
- **Space Complexity**: `O(1)` auxiliary space.
- **Edge Case Missed on First Attempt**:
  Leading, multiple consecutive, and trailing whitespace cleanly handled without extra memory allocation or slice generation.

---

### Problem 3: Count Vowels and Consonants
- **Solution File**: [`problem_3_count_vowels_and_consonants.py`](./problem_3_count_vowels_and_consonants.py)
- **Approach**:
  Maintain a vowel lookup set `{'a', 'e', 'i', 'o', 'u'}` and iterate through string `s`. Accumulate vowel occurrences in `vct` and consonant occurrences in `cct`. Return `1` if vowels strictly exceed consonants, `-1` if consonants strictly exceed vowels, or `0` if their counts match.
- **Time Complexity**: `O(N)` where `N` is the length of `s`.
- **Space Complexity**: `O(1)` auxiliary space.
- **Edge Case Missed on First Attempt**:
  Strings with equal frequencies of vowels and consonants returning `0`, and strings containing only vowels or only consonants.

---

## 💬 Discord Submission Command
```text
/done day7 https://github.com/gameway-sn/DSA_ALPHA_300/blob/main/nov/week-1/07-nov/problem_1_check_if_the_sentence_is_pangram.py https://github.com/gameway-sn/DSA_ALPHA_300/blob/main/nov/week-1/07-nov/problem_2_number_of_segments_in_a_string.py https://github.com/gameway-sn/DSA_ALPHA_300/blob/main/nov/week-1/07-nov/problem_3_count_vowels_and_consonants.py
```
