class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        l = 0
        h = x
        ans = 0
        while l <= h:
            m = (l + h) // 2
            sq = m * m
            if sq == x:
                return m
            elif sq < x:
                ans = m
                l = m + 1
            else:
                h = m - 1

        return ans
