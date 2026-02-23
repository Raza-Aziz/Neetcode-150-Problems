class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        # for i in range(len(nums)):
        #     count = 1
        #     for j in range(i+1, len(nums)):
        #         if i == j:
        #             count += 1
        #     if count == ((len(nums))/2):
        #         return nums[i]

        count = {}
        for n in nums:
            count[n] = count.get(n, 0) + 1

        for k, v in count.items():
            if v > len(nums) / 2:
                return k
