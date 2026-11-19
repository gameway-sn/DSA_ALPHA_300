class Solution:
    def smallestEquivalentString(self, s1: str, s2: str, baseStr: str) -> str:

        parent = [i for i in range(26)]

        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]

        def union(a, b):
            pa = find(a)
            pb = find(b)

            if pa < pb:
                parent[pb] = pa
            else:
                parent[pa] = pb

        for a, b in zip(s1, s2):
            union(ord(a) - 97, ord(b) - 97)

        res = []

        for ch in baseStr:
            root = find(ord(ch) - 97)
            res.append(chr(root + 97))

        return ''.join(res)
