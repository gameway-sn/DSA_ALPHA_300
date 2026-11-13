class Solution:
    def countSegments(self, s: str) -> int:
        
        r = []
        st = 0
        for i in range(len(s)):
            if s[i] == " ":
                r.append(s[st : i])
                st = i + 1

        return r
