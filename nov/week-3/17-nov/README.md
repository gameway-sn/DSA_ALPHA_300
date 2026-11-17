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
- **Solution File**: [`problem_2_count_vowel_substrings_of_a_string.py`](./problem_2_count_vowel_substrings_of_a_string.py)
- **Approach**:
  For every vowel start index `i`, extend `j` rightwards while characters stay vowels, adding each to a `seen` set. Each time `seen` reaches all 5 vowels, that substring `[i..j]` counts, so increment `ans`. A consonant breaks the inner loop, since it ends any all-vowel substring.
- **Time Complexity**: `O(N^2)` worst case (e.g. a long all-vowel string), where `N = len(word)`.
- **Space Complexity**: `O(1)` (`seen` holds at most 5 vowels).
- **Edge Case Missed on First Attempt**:
  None recorded. Substrings must be all vowels, so a consonant breaks the scan, and counting continues for every extension after all 5 vowels are seen.
---

### Problem 3: Prefix Scores of Strings
- **Solution File**: [`problem_3_prefix_scores_of_strings.py`](./problem_3_prefix_scores_of_strings.py)
- **Approach**:
  Build a trie where each node stores `count`, the number of words passing through it. Insert every word, incrementing `count` along its path. Then walk each word again and sum the `count` of every node on its path, which is the number of words sharing each prefix.
- **Time Complexity**: `O(L)` where `L` is the total number of characters across all words.
- **Space Complexity**: `O(L)` for the trie nodes.
- **Edge Case Missed on First Attempt**:
  None recorded. Duplicate words share the same path, so each one's score includes its own copies.
---

## 💬 Discord Submission Command
```text
/done day17 https://github.com/gameway-sn/DSA_ALPHA_300/blob/main/nov/week-3/17-nov/problem_1_maximum_number_of_vowels_in_a_substring_of_given_length.py https://github.com/gameway-sn/DSA_ALPHA_300/blob/main/nov/week-3/17-nov/problem_2_count_vowel_substrings_of_a_string.py https://github.com/gameway-sn/DSA_ALPHA_300/blob/main/nov/week-3/17-nov/problem_3_prefix_scores_of_strings.py
```



