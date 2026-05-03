from typing import List


class Solution:
    def rob(self, nums: List[int]) -> int:

        def rob(i, memo={}):
            if i < 0:
                return 0

            if i in memo:
                return memo[i]

            memo[i] = max(nums[i] + rob(i - 2, memo), rob(i - 1, memo))

            return memo[i]

        amount = rob(len(nums) - 1)

        return amount
