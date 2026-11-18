class Solution:
    def frequencySort(self, s: str) -> str:
        def max_finder(h):
            m = 0
            c = ''
            for k,v in h.items():
                if v > m:
                    m = v
                    c = k
            
            return (c, m)

        h = {}
        r = []
        for c in s:
            h[c] = 1 + h.get(c, 0)

        while len(h) > 0:
            k, v = max_finder(h)
            for i in range(v):
                r.append(k)
            h.pop(k)
        
        return "".join(r)
