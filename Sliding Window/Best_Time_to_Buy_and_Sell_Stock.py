class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """

        L = 0
        R = L + 1
        max_profit = 0

        while R < len(prices):
            profit = prices[R] - prices[L]
            max_profit = max(max_profit, profit)

            if prices[L] < prices[R]:
                R += 1
            else:
                L = R
                R += 1

        return max_profit
