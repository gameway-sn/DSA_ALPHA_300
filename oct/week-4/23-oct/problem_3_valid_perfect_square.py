class Solution(object):
    def isPerfectSquare(self, num):
        """
        :type num: int
        :rtype: bool
        """
        l = 0
        h = num

        while l <= h:
            m = (l + h) // 2
            sq = m * m
            if sq == num:
                return True
            elif sq < num:
                l = m + 1
            else:
                h = m - 1

        return False
