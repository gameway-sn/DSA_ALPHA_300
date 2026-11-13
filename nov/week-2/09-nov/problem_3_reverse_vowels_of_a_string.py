class Solution:
    def reverseVowels(self, s: str) -> str:
        
        v = {'a', 'e', 'i', 'o', 'u'}

        temp = [''] * len(s)

        for i in range(len(s)):
            if s[i].lower() not in v:
                temp[i] = s[i]
        
        i = 0
        j = len(s) - 1

        while i <= j:
            if s[i].lower() not in v:
                i += 1
                continue
            if s[j].lower() not in v:
                j -= 1
                continue
            
            temp[i] = s[j]
            temp[j] = s[i]

            j -= 1
            i += 1

        return "".join(temp)

