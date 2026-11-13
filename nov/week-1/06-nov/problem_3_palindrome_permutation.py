from itertools import permutations

class Solution:
    def allPalindromes(self, s: str) -> list[str]:
        
        def mir(ss):
            r = []
            i = 0
            j = len(ss) - 1
            while j >= i:
                r.append(ss[j])
                j -= 1
            
            return r
        
        # code here
        if len(s) == 1:
            return [s]
        hm = {}
        even = []
        odd = set()
        lf = 0
        for c in s:
            hm[c] = 1 + hm.get(c, 0)

        for k, v in hm.items():
            if v % 2 != 0:
                odd.add(k)
                if v // 2 == 0:
                    even.append(k)
                for i in range(v // 2):
                    even.append(k)
            else:
                for i in range(v // 2):
                    even.append(k)
        
        p = [list(p) for p in permutations(even, len(even))]
        
        r = []
        
        if odd:
            while odd:
                e = odd.pop()
                for w in p:
                    w.extend(e)
                    r.append(w)
        else:
            r = p
            
        l = len(r)
        
        for i in range(l):
            r[i].extend(mir(r[i][0:l]))
            r[i] = "".join(r[i])
        
        return r
