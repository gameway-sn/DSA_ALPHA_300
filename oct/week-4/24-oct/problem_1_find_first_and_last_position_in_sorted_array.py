class Solution(object):
    def searchRange(self, nums, target):
        start = -1
        end = -1

        l = 0
        h = len(nums) - 1

        while l <= h:
            m = (l + h) // 2

            if nums[m] == target:

                # Find first occurrence
                l1 = 0
                h1 = m

                while l1 <= h1:
                    m1 = (l1 + h1) // 2

                    if nums[m1] == target:
                        start = m1
                        h1 = m1 - 1
                    else:
                        l1 = m1 + 1

                # Find last occurrence
                l2 = m
                h2 = len(nums) - 1

                while l2 <= h2:
                    m2 = (l2 + h2) // 2

                    if nums[m2] == target:
                        end = m2
                        l2 = m2 + 1
                    else:
                        h2 = m2 - 1

                return [start, end]

            elif nums[m] < target:
                l = m + 1
            else:
                h = m - 1

        return [-1, -1]
