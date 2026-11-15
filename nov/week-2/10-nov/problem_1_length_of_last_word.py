class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        status = False
        i = len(s) - 1
        r = 0
        
        while i >= 0:
            if s[i].isalpha():
                status = True
                r += 1
            elif status:
                break

            i -= 1

        return r
