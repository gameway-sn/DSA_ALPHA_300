class Solution:
    def reverseWords(self, s: str) -> str:
        def rev(ss):
            return ss[::-1]

        s = s.split()
        r = []

        for w in s:
            r.append(rev(w))
        
        return " ".join(r)
