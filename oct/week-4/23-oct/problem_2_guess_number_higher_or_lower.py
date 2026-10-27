# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num):

class Solution(object):
    def guessNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        l = 1
        h = n

        while l <= h:
            m = (l + h) // 2
            g = guess(m)

            if g == 0:
                return m
            elif g == -1:
                h = m - 1
            else:
                l = m + 1

        return -1
