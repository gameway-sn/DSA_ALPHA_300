class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        h = {}
        
        for i in nums:
            h[i] = 1 + h.get(i, 0)
        
        for k, v in h.items():
            if v > 1:
                return True
        
        return False
