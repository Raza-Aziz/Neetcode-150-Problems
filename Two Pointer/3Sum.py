class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """

        # temp = []
        # st = set()
        # answer = []

        # for i in range(len(nums)):
        #     for j in range(i+1, len(nums)):
        #         for k in range(j+1, len(nums)):
        #             if (nums[i] + nums[j] + nums[k] == 0):
        #                 temp = [nums[i], nums[j], nums[k]]
        #                 new_temp = sorted(temp)
        #                 st.add(tuple(new_temp))

        # answer.extend(st)
        # return answer

        # st = set()
        # answer = []

        # for i in range(len(nums)):
        #     hash_set = set()

        #     for j in range(i+1, len(nums)):
        #         k = (nums[i] + nums[j]) * -1

        #         if k in hash_set:
        #             temp = [nums[i], nums[j], k]
        #             temp = sorted(temp)
        #             st.add(tuple(temp))

        #         else:
        #             hash_set.add(nums[j])

        # answer.extend(st)
        # return answer

        # issue 1
        nums = sorted(nums)
        result = []
        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            j = i + 1
            k = len(nums) - 1

            while j < k:
                ans = nums[i] + nums[j] + nums[k]
                if ans > 0:
                    k -= 1
                elif ans < 0:
                    j += 1

                else:
                    temp = [nums[i], nums[j], nums[k]]
                    # issue 3 (extend instead of append)
                    result.append(temp)
                    j += 1
                    k -= 1

                    # issue 2
                    while j < k and nums[k] == nums[k + 1]:
                        k -= 1
                    while j < k and nums[j] == nums[j - 1]:
                        j += 1

        return result
