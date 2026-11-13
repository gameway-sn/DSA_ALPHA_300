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

### Problem 2: Longest Palindrome (count chars)
- **Solution File**: [`problem_2_longest_palindrome_count_chars.py`](./problem_2_longest_palindrome_count_chars.py)
- **Approach**:
  Count character frequencies in `s` manually via a hash dictionary. Sum up all even counts and the even component (`v - 1`) of any odd counts. If any character appears an odd number of times, place one odd character at the center of the palindrome by adding 1 to the final length.
- **Time Complexity**: `O(N)` where `N` is `len(s)`.
- **Space Complexity**: `O(1)` auxiliary space (at most 52 English letters).
- **Edge Case Missed on First Attempt**:
  Strings where all characters have odd frequencies (e.g., `"aaaaa"` yielding full length 5, or all unique characters `"abc"` yielding length 1).

---

### Problem 3: Palindrome Permutation
- **Solution File**: [`problem_3_palindrome_permutation.py`](./problem_3_palindrome_permutation.py)
- **Approach**:
  Extract character frequencies into hash map `hm`, partitioning characters into half-counts for the prefix and tracking odd central characters. Permute the prefix characters, attach the odd central character when present, and mirror the prefix using a custom manual two-pointer reversal function `mir` without using `[::-1]`.
- **Time Complexity**: $O(K! \cdot K)$ where $K$ is the number of half-characters permuted.
- **Space Complexity**: $O(K! \cdot K)$ to store permutations and mirrored outputs.
- **Edge Case Missed on First Attempt**:
  Strings with more than one odd-frequency character which cannot form any valid palindrome permutations, and deduplicating permutations when multi-count identical characters are permuted.

---

## 💬 Discord Submission Command
```text
/done day6 https://github.com/gameway-sn/DSA_ALPHA_300/blob/main/nov/week-1/06-nov/problem_1_valid_palindrome_ii_allow_1_deletion.py https://github.com/gameway-sn/DSA_ALPHA_300/blob/main/nov/week-1/06-nov/problem_2_longest_palindrome_count_chars.py https://github.com/gameway-sn/DSA_ALPHA_300/blob/main/nov/week-1/06-nov/problem_3_palindrome_permutation.py
```
