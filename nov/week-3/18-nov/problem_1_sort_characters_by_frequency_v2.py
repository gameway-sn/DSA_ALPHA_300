class Solution:
    def frequencySort(self, s: str) -> str:
        h = {}
        r = []
        
        for c in s:
            h[c] = 1 + h.get(c, 0)

        b = [[] for _ in range(len(s) + 1)]

        for k,v in h.items():
            b[v].append(k)
        #print(b)
        for i in range(len(s), 0, -1):
            for c in b[i]:
                r.append(c*i)

        return "".join(r)
