class Solution(object):
    def findValidPair(self, s):
        """
        :type s: str
        :rtype: str
        """

        count = {}
        for n in s:
            count[n] = count.get(n, 0) + 1

        for i in range(len(s) - 1):
            first = s[i]
            second = s[i + 1]

            if first != second:
                if int(first) == count[first] and int(second) == count[second]:
                    return first + second
        return ""


# Explanation:
#   - Use hashing (hash map) to count digit frequencies
#   1. Iterate through the string and store frequency of each digit in a dict
#   2. Traverse the string again and check every adjacent pair
#   3. If both digits in the pair equal their total frequency in the string,
#      return the pair in original order
#   4. If no valid adjacent pair is found, return an empty string
