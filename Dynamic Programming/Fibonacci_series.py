class Solution:
    def fib(self, n: int) -> int:
        # if n == 0 or n == 1:
        #     return n

        # return self.fib(n - 1) + self.fib(n - 2)

        # DP + Tabulation + Space Optimization
        prev_1 = 0
        prev_2 = 1

        if n == 0:
            return 0

        for i in range(2, n + 1):
            curr = prev_1 + prev_2

            prev_1 = prev_2
            prev_2 = curr

        return prev_2

    # Using Memoization + Recursion
    def fib_recursive(self, n: int, fibd={}) -> int:

        if n == 0 or n == 1:
            return n

        if n in fibd:
            return fibd[n]

        n_1 = self.fib(n - 1, fibd)
        n_2 = self.fib(n - 2, fibd)
        result = n_1 + n_2

        fibd[n] = result

        return result
