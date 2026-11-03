class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        hm = {}

        for i in range(len(s)):
            c = s[i]
            if c in hm:
                hm.pop(c)
            else:
                hm[c] = i
        
        r = float('inf')
        
        for k, v in hm.items():
            if v < r:
                r = v
        
        return r if r != float('inf') else -1

