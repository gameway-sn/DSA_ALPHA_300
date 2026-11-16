class Solution:
    def characterReplacement(self, s: str, k: int) -> int:

        h = {}
        i = 0
        m = 0
        r = 0

        for j in range(len(s)):

            h[s[j]] = h.get(s[j], 0) + 1
            m = max(m, h[s[j]])

            while (j - i + 1) - m > k:
                h[s[i]] -= 1
                i += 1

            r = max(r, j - i + 1)

        return r
