class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """

        seen = set()
        for n in nums:
            if n in seen:
                return True
            else:
                seen.add(n)
        return False


# Explanation:
# - Again, use hashing (Hash set)
#   1. Iterate through the array
#   2. Check if num is in set
#   2.1 IF exists: return True as already present before in array
#   2.2 ELSE: Just add in set
