class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """

        # count = {}
        # storing or pre-compute
        # for n in nums:
        #   count[n] = 1 + count.get(n, 0)

        # retrieval
        # result = []
        # for n, _ in sorted(count.items(), key=lambda counts: counts[1], reverse=True):
        #     result.append(n)

        # return result[:k]

        # --OPTIMAL SOLUTION:
        counts = {}

        for n in nums:
            counts[n] = counts.get(n, 0) + 1

        freq = [[] for i in range(len(nums) + 1)]

        for num, count in counts.items():
            freq[count].append(num)

        res = []

        for i in range(len(freq) - 1, 0, -1):
            for n in freq[i]:
                res.append(n)
                if len(res) == k:
                    return res
