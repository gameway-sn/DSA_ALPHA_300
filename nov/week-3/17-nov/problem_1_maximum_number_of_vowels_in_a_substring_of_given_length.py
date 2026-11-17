class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        v = {'a', 'e', 'i', 'o', 'u'}

        if len(s) < k:
            return 0

        ts = 0

        for i in range(k):
            if s[i] in v:
                ts += 1

        c = ts

        for i in range(1, len(s) - k + 1):
            if s[i-1] in v:
                ts -= 1

            if s[i+k-1] in v:
                ts += 1

            c = max(c, ts)

        return c
