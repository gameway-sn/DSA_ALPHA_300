class Solution:
    def reverseWords(self, s: str) -> str:
        s = s.split()
        r = []
        for i in range(len(s) - 1, -1, -1):
            r.append(s[i])
        
        return " ".join(r)

