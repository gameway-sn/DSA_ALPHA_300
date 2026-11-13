class Solution:
    def reverseOnlyLetters(self, s: str) -> str:
        def rev(ss):
            return ss[::-1]

        def rev2(l):
            temp = [""] * len(l)
            
            for i in range(len(l)):
                if not l[i].isalpha():
                    temp[i] = l[i]
            i = 0
            j = len(l) - 1

            while i <= j:
                if not l[i].isalpha():
                    i += 1
                    continue
                if not l[j].isalpha():
                    j -= 1
                    continue

                temp[i] = l[j]
                temp[j] = l[i] 
                i += 1
                j -= 1

            return temp

        r = []
        t = []

        for c in s:
            if c.isalpha():
                t.append(c)
                continue

            r.extend(t)
            t = []
            r.extend([c])
        if t:
            r.extend(t)
        
        r = rev2(r)
        
        return "".join(r)

