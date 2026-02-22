class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """

        s_freq = {}
        t_freq = {}

        for s_char in s:
            # One-liner way to do
            # s_freq[s_char] = s_freq.get(s_char, 0) + 1

            if s_char not in s_freq:
                s_freq[s_char] = 1
            else:
                s_freq[s_char] += 1

        for t_char in t:
            if t_char not in t_freq:
                t_freq[t_char] = 1
            else:
                t_freq[t_char] += 1

        if t_freq == s_freq:
            return True
        else:
            return False


# Explanation:
#   - Use hashing (hash map)
#   1. Iterate through s and t strings individually
#   2. Simply store freq of each char in respective dicts
#   3. Finally, check equality of both dicts
