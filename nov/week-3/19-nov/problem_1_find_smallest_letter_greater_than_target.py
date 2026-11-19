class Solution:
    def nextGreatestLetter(self, letters: list[str], target: str) -> str:
        
        
        l = 0
        h = len(letters) -1

        while l < h-1:
            m = (l + h)//2
            if letters[m] == target:
                l = m + 1
            elif letters[m] < target:
                l = m
            elif letters[m] > target:
                h = m

        r = '}'
        for c in (letters[l : h+1]):
            if c > target:
                r = min(r, c)

        return r if r != '}' else letters[0]
