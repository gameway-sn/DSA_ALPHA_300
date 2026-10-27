# Day 23 · 23-oct (Fri)

**Topic**: Binary search on answer  
**DON'T REACH FOR**: `bisect, math.isqrt(). Build the condition check inside your BS.`

---

## 📝 Problems & Solutions

### Problem 1: Sqrt(x)
- **Solution File**: [`problem_1_sqrt_x.py`](./problem_1_sqrt_x.py)
- **Approach**:
  Binary search on the answer space in the range `[0, x]`. For candidate root `m`, compute `sq = m * m`. If `sq == x`, return `m` immediately. If `sq < x`, record `m` as a valid candidate (`ans = m`) and search the higher half (`l = m + 1`); otherwise search the lower half (`h = m - 1`).
- **Time Complexity**: `O(log X)`
- **Space Complexity**: `O(1)`
- **Edge Case Missed on First Attempt**:
  Handling boundary inputs `x = 0` and `x = 1`, and correctly preserving the floor integer square root (`ans`) when `x` is not a perfect square.

---

### Problem 2: Guess Number Higher or Lower
- **Solution File**: [`problem_2_guess_number_higher_or_lower.py`](./problem_2_guess_number_higher_or_lower.py)
- **Approach**:
  Binary search across the 1-indexed range `[1, n]`. Query the pre-defined `guess(m)` API: if `0`, the picked number is found; if `-1`, the pick is strictly smaller so shrink the upper bound (`h = m - 1`); if `1`, the pick is strictly larger so increase the lower bound (`l = m + 1`).
- **Time Complexity**: `O(log N)`
- **Space Complexity**: `O(1)`
- **Edge Case Missed on First Attempt**:
  Starting lower bound at `1` rather than `0` (numbers are 1-indexed), and checking the binary search loop condition `l <= h` instead of `l <= n`.

---

## 💬 Discord Submission Command
```text
/done day23 https://github.com/gameway-sn/DSA_ALPHA_300/blob/main/oct/week-4/23-oct/problem_1_sqrt_x.py https://github.com/gameway-sn/DSA_ALPHA_300/blob/main/oct/week-4/23-oct/problem_2_guess_number_higher_or_lower.py https://github.com/gameway-sn/DSA_ALPHA_300/blob/main/oct/week-4/23-oct/problem_3_valid_perfect_square.py
```
