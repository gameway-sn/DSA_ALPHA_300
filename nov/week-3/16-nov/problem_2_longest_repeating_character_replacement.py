# not correct this ignores the last index window checking and window tracking is wrong since we are using abs because abs(i-j) give index diff but we want length j-i+1 is the window length
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        
        h = {}
        i = 0
        j = 0
        r = 0
        m = 0
        
        while j < len(s):
            print(h, i, j, m)
            if ((abs(i - j)) - m) > k:
                h[s[i]] -= 1
                i += 1
                continue
            h[s[j]] = 1 + h.get(s[j], 0)
            m = max(h[s[j]], m)
            r = max(abs(i - j), r)
            j += 1
        return r
