class Solution(object):
    def commonChars(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """
        r = []
        h = {}
        strs = words
        for c in words[0]:
            h[c] = 1 + h.get(c, 0)

        for i in range(1, len(strs)):
            ht = {}
            
            for c in strs[i]:
                if h == ht:
                    break
                if c in h:
                    ht[c] = 1 + ht.get(c, 0)
                
            for k, v in list(h.items()):
                if k not in ht:
                    h.pop(k)
                else:
                    if ht[k] < h[k]:
                        h[k] = ht[k]

        for k, v in h.items():
            for i in range(v):
                r.append(k)

        return r

