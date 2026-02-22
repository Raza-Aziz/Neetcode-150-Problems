class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """

        # -- OPTIMAL
        result = []
        dic = {}
        for i in range(len(nums)):
            a = nums[i]
            b = target - a
            if b not in dic:
                dic[a] = i
            else:
                result.append(i)
                result.append(dic.get(b))
                return result

        # -- BRUTE FORCE
        # for i in range(len(nums)):
        #     for j in range(i+1, len(nums)):
        #         if (nums[i] + nums[j] == target):
        #             result.append(i)
        #             result.append(j)
        #             return result


# Explanation (For OPTIMAL):
# - Use hashing
#   1. Iterate through array (i)
#   2. Check if target - a exists in map (which means already iterated through in loop)
#   3.1. IF exists: simply append in result array and return
#   3.2. ELSE (not exists): append number (a) in dict and continue
#       - So that when it's time for (b) in loop, we can retrieve (a) as it exists
