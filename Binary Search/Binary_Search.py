class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """

        l = 0
        r = len(nums) - 1

        while l + 1 < r:  # Check if array has atleast 3 elements
            m = (l + r) // 2

            if nums[m] == target:
                return m
            elif nums[m] < target:
                l = m
            else:
                r = m

        # So array is less than 3 elements (case of 1 element)
        if nums[l] == target:
            return l
        if nums[r] == target:
            return r

        return -1
