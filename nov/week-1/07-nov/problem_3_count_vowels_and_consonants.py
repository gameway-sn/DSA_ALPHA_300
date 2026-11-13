class Solution:
    def checkString(self, s: str) -> int:
        # code here
        v = {'a', 'e', 'i', 'o', 'u'}
        vct = 0
        cct = 0
        for c in s:
            if c in v:
                vct += 1
            else:
                cct += 1
        
        if vct == cct:
            return 0
        elif vct < cct:
            return -1
        else:
            return 1
