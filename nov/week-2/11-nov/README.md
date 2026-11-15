# Day 11 · 11-nov (Wed)

**Topic**: String rotation  
**DON'T REACH FOR**: `s in (s+s). Build the rotation check with modular index walk.`

---

## 📝 Problems & Solutions

### Problem 1: Rotate String
- **Solution File**: [`problem_1_rotate_string.py`](./problem_1_rotate_string.py)
- **Approach**:
  Verify length equality between `s` and `goal`. Scan `s` to locate a candidate shift offset `diff` by comparing neighboring characters to `goal[1]` and `goal[-1]`. Traverse circular indices from `diff` checking character equality with `goal[j]`.
- **Time Complexity**: `O(N)` where `N` is the length of `s`.
- **Space Complexity**: `O(1)` auxiliary space.
- **Edge Case Missed on First Attempt**:
  Strings with multiple identical candidate characters (e.g. `s = "abac", goal = "acab"` or strings with duplicate prefixes), where local neighbor checking can select an incorrect rotation offset `diff`. Trying each matching index with a full modular index walk `(i + j) % n == goal[j]` handles all repeated patterns reliably.

#### Alternative Solution (v2)
- **Solution File**: [`problem_1_rotate_string_v2.py`](./problem_1_rotate_string_v2.py)
- **Approach**:
  Check length equality `len(s) == len(goal)`. Directly check substring inclusion `goal in s + s`, since every cyclic shift of a string of length $N$ is contained as a contiguous substring within $s + s$.
- **Time Complexity**: `O(N)` where `N` is the length of `s`.
- **Space Complexity**: `O(N)` to construct the doubled string `s + s`.
- **Edge Case Missed on First Attempt**:
  Length mismatch check prevents false positive matches on unequal strings. *(Note: `goal in s + s` is the classic Python shortcut; comparison with v1 demonstrates manual circular traversal).*

---

## 💬 Discord Submission Command
```text
/done day11 https://github.com/gameway-sn/DSA_ALPHA_300/blob/main/nov/week-2/11-nov/problem_1_rotate_string.py https://github.com/gameway-sn/DSA_ALPHA_300/blob/main/nov/week-2/11-nov/problem_2_shift_2d_grid_as_string_chars.py https://github.com/gameway-sn/DSA_ALPHA_300/blob/main/nov/week-2/11-nov/problem_3_rotate_string_by_k.py
```
