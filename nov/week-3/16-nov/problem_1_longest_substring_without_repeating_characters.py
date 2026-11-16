class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        w = set()
        r = 0
        i = 0
        j = 0
        while j < len(s):
            if s[j] in w:
                w.remove(s[i])
                i += 1
                continue
            w.add(s[j])
            r = max(len(w), r)
            j += 1

        return r
