class Solution:
    def customSortString(self, order: str, s: str) -> str:
        
        h = {}

        for c in s:
            h[c] = 1 + h.get(c, 0)
        
        r = []

        for c in order:
            if c in h:
                r.append(c * h[c])
                h.pop(c)
        #print(r, h)
        for k, v in h.items():
            r.append(k * v)


        return "".join(r)
