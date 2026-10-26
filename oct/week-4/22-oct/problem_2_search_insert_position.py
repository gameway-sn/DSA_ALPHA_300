class Solution(object):
    def searchInsert(self, nums, target):
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
            elif n > target:
                h = m - 1

        return l
