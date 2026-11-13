class Solution:
    def countSegments(self, s: str) -> int:
        if not s:
            return 0
        i = 0
        r = 0
        prev = False
        for c in s:
            if c != " " and not prev:
                r += 1
                prev = True
            if c == " ":
                prev = False
        
        return r
