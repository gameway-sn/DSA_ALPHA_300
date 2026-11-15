class Solution:
    def shortestToChar(self, s: str, c: str) -> list[int]:
        i = 0
        prev = float('-inf')
        r = [0] * len(s)

        for i in range(len(s)):
            if s[i] == c:
                prev = i
            r[i] = abs(i - prev)

        prev = float("inf")
        for j in range(len(s) - 1, -1, -1):
            if s[j] == c:
                prev = j
            r[j] = min(r[j], abs(j - prev))

        return r
