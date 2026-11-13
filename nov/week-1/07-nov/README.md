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

## 💬 Discord Submission Command
```text
/done day7 https://github.com/gameway-sn/DSA_ALPHA_300/blob/main/nov/week-1/07-nov/problem_1_check_if_the_sentence_is_pangram.py https://github.com/gameway-sn/DSA_ALPHA_300/blob/main/nov/week-1/07-nov/problem_2_number_of_segments_in_a_string.py https://github.com/gameway-sn/DSA_ALPHA_300/blob/main/nov/week-1/07-nov/problem_3_count_vowels_and_consonants.py
```
