class Solution(object):
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        i = 2
        w = "1"
        while i <= n:
            r = []
            ct = 0
            e = w[0]
            for c in w:
                if e == c:
                    ct += 1
                else:
                    t = str(ct) + e
                    r.append(t)
                    ct = 1
                    e = c
            t = str(ct) + e
            r.append(t)
            w = "".join(r)
            i += 1

        return w

