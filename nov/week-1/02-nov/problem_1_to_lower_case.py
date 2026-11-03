class Solution(object):
    def toLowerCase(self, s):
        """
        :type s: str
        :rtype: str
        """
        l = list(s)
        r = []
        
        for i in l:
            e = ord(i)

            if e < 91 and e > 64:
                r.append(chr(e + 32))
            else:
                r.append(i)
        
        return "".join(r)

