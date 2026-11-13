class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        def rev(ss):
            return ss[::-1]

        r = []
        loc = 0
        for i in range(len(word)):
            if word[i] == ch:
                r.append(rev(word[:i + 1]))
                loc = i
                break
        
        if loc == 0:
            return word
            
        r.append(word[loc + 1:])

        return "".join(r)
