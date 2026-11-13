# Day 6 · 06-nov (Fri)

**Topic**: Palindrome variants  
**DON'T REACH FOR**: `s[::-1], reversed(). Build your own reverse (same as Oct Day 9).`

---

## 📝 Problems & Solutions

### Problem 1: Valid Palindrome II (allow 1 deletion)
- **Solution File**: [`problem_1_valid_palindrome_ii_allow_1_deletion.py`](./problem_1_valid_palindrome_ii_allow_1_deletion.py)
- **Approach**:
  Traverse with two pointers `i` and `j` moving inward from both ends. Upon the first character mismatch (`s[i] != s[j]`), check whether removing the left character (`s[i+1 : j+1]`) or the right character (`s[i:j]`) forms a palindrome. The helper palindrome check uses a two-pointer walk instead of `s[::-1]`.
- **Time Complexity**: `O(N)` where `N` is `len(s)`.
- **Space Complexity**: `O(N)` for slice allocation during the one allowed deletion check.
- **Edge Case Missed on First Attempt**:
  Asymmetric mismatch cases where deleting one branch fails while the alternate branch succeeds (e.g., `"abca"` vs `"cupuufxoohdfpgjdmysgvhmvffcnqxjjxqncffvmhvgsymdjgpfdhooxfuupuc"`).

---

## 💬 Discord Submission Command
```text
/done day6 https://github.com/gameway-sn/DSA_ALPHA_300/blob/main/nov/week-1/06-nov/problem_1_valid_palindrome_ii_allow_1_deletion.py https://github.com/gameway-sn/DSA_ALPHA_300/blob/main/nov/week-1/06-nov/problem_2_longest_palindrome_count_chars.py https://github.com/gameway-sn/DSA_ALPHA_300/blob/main/nov/week-1/06-nov/problem_3_palindrome_permutation.py
```
