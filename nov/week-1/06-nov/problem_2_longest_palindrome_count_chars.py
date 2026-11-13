class Solution:
    def longestPalindrome(self, s: str) -> int:
        hs = {}
        if len(s) == 1:
            return 1
        elif len(s) == 0:
            return 0

        for c in s:
            hs[c] = 1 + hs.get(c, 0)

        r = 0
        odd = False
        for k, v in hs.items():
            if v % 2 == 0:
                r += v
            else:
                odd = True
                r += v - 1
        
        return r + 1 if odd else r
