# Day 10 · 10-nov (Tue)

**Topic**: Split, trim, rejoin  
**DON'T REACH FOR**: `s.split() with no args — fine. But build the loop version too, and compare.`

---

## 📝 Problems & Solutions

### Problem 1: Length of Last Word
- **Solution File**: [`problem_1_length_of_last_word.py`](./problem_1_length_of_last_word.py)
- **Approach**:
  Loop backwards from `len(s) - 1` down to `0`. Skip trailing whitespace until the first alphabetic character is encountered, toggling `status = True` and incrementing length `r`. Break out of the loop upon encountering the subsequent whitespace delimiter, achieving $O(1)$ space without using `split()`.
- **Time Complexity**: `O(N)` where `N` is the length of `s`.
- **Space Complexity**: `O(1)` auxiliary space.
- **Edge Case Missed on First Attempt**:
  Strings ending with multiple trailing spaces (e.g. `"a "` or `"fly me to the moon "`), handled by deferring word counting until the first non-space character is seen.

---

### Problem 2: Shortest Distance to a Character
- **Solution File**: [`problem_2_shortest_distance_to_a_character.py`](./problem_2_shortest_distance_to_a_character.py)
- **Approach**:
  Maintain two pointers `prev` and `j` tracking the most recent and next occurrence of target character `c`. For each index `i`, compute the minimum absolute distance to either occurrence `min(|i - j|, |i - prev|)`, advancing `j` and shifting `prev = j` whenever `i > j`.
- **Time Complexity**: `O(N)` where `N` is the length of `s`.
- **Space Complexity**: `O(1)` auxiliary space (excluding output array `r`).
- **Edge Case Missed on First Attempt**:
  Indices before the first occurrence of `c` and indices past the final occurrence of `c`, where only one boundary is within string limits.

#### Alternative Solution (v2)
- **Solution File**: [`problem_2_shortest_distance_to_a_character_v2.py`](./problem_2_shortest_distance_to_a_character_v2.py)
- **Approach**:
  Standard two-pass array scan. Pass 1 sweeps left-to-right recording distances from the most recent occurrence of `c` (`prev = float('-inf')`). Pass 2 sweeps right-to-left recording distances from the closest upcoming occurrence of `c` (`prev = float('inf')`), updating each position with `min(r[j], |j - prev|)`.
- **Time Complexity**: `O(N)` where `N` is the length of `s`.
- **Space Complexity**: `O(1)` auxiliary space (excluding output array `r`).
- **Edge Case Missed on First Attempt**:
  Positions occurring before the initial appearance of `c` cleanly resolve during the backwards pass.

---

## 💬 Discord Submission Command
```text
/done day10 https://github.com/gameway-sn/DSA_ALPHA_300/blob/main/nov/week-2/10-nov/problem_1_length_of_last_word.py https://github.com/gameway-sn/DSA_ALPHA_300/blob/main/nov/week-2/10-nov/problem_2_shortest_distance_to_a_character.py https://github.com/gameway-sn/DSA_ALPHA_300/blob/main/nov/week-2/10-nov/problem_3_goal_parser_interpretation.py
```
