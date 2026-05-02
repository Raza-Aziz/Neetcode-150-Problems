class Solution:
    def climbStairs(self, n: int, ways={}) -> int:
        # Solution 1 : Using recursion

        # Base case
        if n <= 0:
            return 0
        if n == 1:
            return 1
        if n == 2:
            return 2

        # most important
        if n in ways:
            return ways[n]

        way_1 = self.climbStairs(n - 1)
        way_2 = self.climbStairs(n - 2)
        way_n = way_1 + way_2

        ways[n] = way_n

        return ways[n]
