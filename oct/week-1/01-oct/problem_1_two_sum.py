class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        h = {}

        for j, i in enumerate(nums):
            c = target - i

            if c in h:
                return [h[c], j]

            h[i] = j
