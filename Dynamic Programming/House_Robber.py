from typing import List


class Solution:
    def rob(self, nums: List[int]) -> int:

        def solve(i, memo={}):
            if i < 0:
                return 0

            if i in memo:
                return memo[i]

            memo[i] = max(nums[i] + solve(i - 2, memo), solve(i - 1, memo))

            return memo[i]

        amount = solve(len(nums) - 1)

        return amount
