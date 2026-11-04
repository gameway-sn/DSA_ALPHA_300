class Solution(object):
    def intersection(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        num1 = set(nums1)
        num2 = set(nums2)
        r = []

        while num1 and num2:
            t = num2.pop()
            if t in num1:
                r.append(t)
                num1.remove(t)

        return r
