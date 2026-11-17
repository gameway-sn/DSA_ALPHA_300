# Day 17 · 17-nov (Tue)

**Topic**: Prefix sum on strings (echo of Oct Day 6)  
**DON'T REACH FOR**: `itertools.accumulate(). Build the prefix count array yourself.`

---

## 📝 Problems & Solutions

### Problem 1: Maximum Number of Vowels in a Substring of Given Length
> Submitted in the Day 17 Q1 slot (curriculum lists *Number of Vowels in Substring Ranges (prefix-count)* here).
- **Solution File**: [`problem_1_maximum_number_of_vowels_in_a_substring_of_given_length.py`](./problem_1_maximum_number_of_vowels_in_a_substring_of_given_length.py)
- **Approach**:
  Fixed-size sliding window of length `k`. Count vowels in the first window into `ts`, then slide one step at a time: subtract 1 if the outgoing character `s[i-1]` is a vowel, add 1 if the incoming character `s[i+k-1]` is a vowel, and track the maximum in `c`.
- **Time Complexity**: `O(N)` where `N = len(s)`.
- **Space Complexity**: `O(1)` (fixed 5-element vowel set).
- **Edge Case Missed on First Attempt**:
  None recorded. Guarded `len(s) < k` returning `0`, and the slide loop bound `range(1, len(s) - k + 1)` covers every window exactly once.

---

### Problem 2: Count Vowel Substrings of a String
- _Pending — not yet submitted._

---

### Problem 3: Prefix Scores of Strings
- _Pending — not yet submitted._

---

## 💬 Discord Submission Command
_Pending — problems 1 and 3 still need to be submitted._

