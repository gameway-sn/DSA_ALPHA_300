class Solution:
    def reverseVowels(self, s: str) -> str:

        v = {'a', 'e', 'i', 'o', 'u'}
        temp = list(s)

        i, j = 0, len(s) - 1

        while i < j:
            if temp[i].lower() not in v:
                i += 1
            elif temp[j].lower() not in v:
                j -= 1
            else:
                temp[i], temp[j] = temp[j], temp[i]
                i += 1
                j -= 1

        return "".join(temp)

