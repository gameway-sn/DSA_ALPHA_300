# not optimal
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        i = 0
        
        while i < len(haystack):
            print(haystack[i: len(needle)])
            if haystack[i: i + len(needle)] == needle:
                return i
            i += 1
            
        return -1

