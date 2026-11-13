class Solution:
    def validPalindrome(self, s: str) -> bool:
        
        def pal(ss):
            i = 0
            j = len(ss) - 1
            while i < j:
                if ss[i] != ss[j]:
                    return False
                i += 1
                j -= 1
            return True

        i = 0
        j = len(s) - 1
        st = 0
        while i <= j:
            if s[i] != s[j]:
                return (pal(s[i+1 : j+1]) or pal(s[i:j]))
            
            i += 1
            j -= 1
            
        return True

