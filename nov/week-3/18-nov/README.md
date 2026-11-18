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

---

## 💬 Discord Submission Command
```text
/done day18 https://github.com/gameway-sn/DSA_ALPHA_300/blob/main/nov/week-3/18-nov/problem_1_sort_characters_by_frequency.py <link_to_prob_2> <link_to_prob_3>
```
