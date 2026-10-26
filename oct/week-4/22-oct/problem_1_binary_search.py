class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        l = 0
        h = len(nums) - 1

        while l <= h:
            m = (l + h) // 2
            n = nums[m]
            if n == target:
                return m
            elif n < target:
                l = m + 1
            else:
                h = m - 1

        return -1
