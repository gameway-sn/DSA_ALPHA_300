class Solution:
    def shortestToChar(self, s: str, c: str) -> list[int]:
        r = []
        i = 0
        j = 0
        prev = len(s) - 1

        while i < len(s): 
            while j < len(s) and s[j] != c:
                j += 1
            
            if j < len(s):
                r.append(min(abs(i - j), abs(i - prev)))
            else:
                r.append(abs(i - prev))
            i += 1
            if i > j:
                prev = j
                j += 1                

        return r
