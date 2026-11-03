class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        hms, hmt = {}, {}
        if len(s) != len(t):
            return False
        
        for i in range(len(s)):
            hms[s[i]] = 1 + hms.get(s[i], 0)
            hmt[t[i]] = 1 + hmt.get(t[i], 0)

        return hmt == hms
