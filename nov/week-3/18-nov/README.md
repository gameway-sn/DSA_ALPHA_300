# Day 18 · 18-nov (Wed)

**Topic**: Sort on strings (uses YOUR OWN sort from Oct Week 3)  
**DON'T REACH FOR**: `sorted(), .sort(). Use your own merge/quick sort.`

---

## 📝 Problems & Solutions

### Problem 1: Sort Characters By Frequency
- **Solution File**: [`problem_1_sort_characters_by_frequency.py`](./problem_1_sort_characters_by_frequency.py)
- **Approach**:
  Count each character's frequency in a hash map. Then repeatedly run a selection-style scan (`max_finder`) to pull out the character with the highest remaining count, append it that many times to the result, and remove it from the map. No built-in sort is used.
- **Time Complexity**: `O(N + U^2)` where `N = len(s)` and `U` is the number of distinct characters (`U` is bounded by the alphabet size, so effectively `O(N)`).
- **Space Complexity**: `O(N)` for the result list (plus `O(U)` for the map).
- **Edge Case Missed on First Attempt**:
  None recorded. `max_finder` starts at `m = 0` and uses strict `>`, so ties are broken arbitrarily, which is valid for this problem.

#### Alternative Solution (v2)
- **Solution File**: [`problem_1_sort_characters_by_frequency_v2.py`](./problem_1_sort_characters_by_frequency_v2.py)
- **Approach**:
  Bucket sort by frequency. Count characters in a hash map, then place each character into bucket `b[count]` (buckets `0..len(s)`). Walk the buckets from highest count down to 1 and append `char * count` for every character in each bucket. No repeated max scans are needed.
- **Time Complexity**: `O(N)` where `N = len(s)`.
- **Space Complexity**: `O(N)` for the buckets and result.
- **Edge Case Missed on First Attempt**:
  None recorded. Buckets are sized `len(s) + 1` so a single repeated character (count `N`) fits, and the loop stops at 1 since no character has count 0.

---

### Problem 3: Custom Sort String
- **Solution File**: [`problem_3_custom_sort_string.py`](./problem_3_custom_sort_string.py)
- **Approach**:
  Count the characters of `s` in a hash map. Walk `order` and, for each character present in the map, append it repeated by its count, then remove it from the map. Whatever is left in the map (characters not in `order`) is appended at the end in any order. No built-in sort is used.
- **Time Complexity**: `O(N + M)` where `N = len(s)` and `M = len(order)`.
- **Space Complexity**: `O(N)` for the result (plus `O(1)` for the map, bounded by the alphabet).
- **Edge Case Missed on First Attempt**:
  None recorded. Characters in `order` but absent from `s` are skipped via the `in h` check, and characters of `s` missing from `order` are still appended.

---

## 💬 Discord Submission Command
```text
/done day18 https://github.com/gameway-sn/DSA_ALPHA_300/blob/main/nov/week-3/18-nov/problem_1_sort_characters_by_frequency.py <link_to_prob_2> https://github.com/gameway-sn/DSA_ALPHA_300/blob/main/nov/week-3/18-nov/problem_3_custom_sort_string.py
```
