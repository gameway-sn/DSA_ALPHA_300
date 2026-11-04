# Day 4 · 04-nov (Wed)

**Topic**: Char counting advanced (two-string compare)  
**DON'T REACH FOR**: `Counter, Counter arithmetic. Two dicts, manual compare.`

---

## 📝 Problems & Solutions

### Problem 1: Ransom Note
- **Solution File**: [`problem_1_ransom_note.py`](./problem_1_ransom_note.py)
- **Approach**:
  Populate a frequency dictionary `hm` for all characters in `magazine` manually using `.get(i, 0)` without importing `Counter`. Iterate through each character `c` of `ransomNote`, decrementing its available count in `hm`; return `False` if `c` is absent or its remaining frequency drops below zero. Return `True` once all required characters are satisfied.
- **Time Complexity**: `O(M + N)` where `M` is `len(magazine)` and `N` is `len(ransomNote)`.
- **Space Complexity**: `O(1)` auxiliary space (at most 26 lowercase English letters).
- **Edge Case Missed on First Attempt**:
  Characters present in `magazine` but insufficient in quantity for `ransomNote` (e.g. `ransomNote = "aa"`, `magazine = "a"`), handled by decrementing counts and checking exhaustion.

---

### Problem 2: Find Common Characters
- **Solution File**: [`problem_2_find_common_characters.py`](./problem_2_find_common_characters.py)
- **Approach**:
  Initialize a frequency map from the first word. For each subsequent word, count character frequencies in a temporary dictionary `ht` and update the base map by retaining the minimum common frequency (or removing absent keys). Expand each surviving character by its final count into the result list.
- **Time Complexity**: `O(N \cdot L)` where `N` is the number of words and `L` is the average word length.
- **Space Complexity**: `O(1)` auxiliary space (bounded by 26 English letters).
- **Edge Case Missed on First Attempt**:
  Characters present in earlier words but entirely absent in later words (which must be eliminated with frequency 0), and safe dictionary iteration without mutating dict size mid-loop.

---

## 💬 Discord Submission Command
```text
/done day4 https://github.com/gameway-sn/DSA_ALPHA_300/blob/main/nov/week-1/04-nov/problem_1_ransom_note.py https://github.com/gameway-sn/DSA_ALPHA_300/blob/main/nov/week-1/04-nov/problem_2_find_common_characters.py https://github.com/gameway-sn/DSA_ALPHA_300/blob/main/nov/week-1/04-nov/problem_3_jewels_and_stones.py
```
