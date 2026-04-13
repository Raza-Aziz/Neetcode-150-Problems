class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """

        stack = []
        closed_to_open = {")": "(", "}": "{", "]": "["}

        for bracket in s:
            if bracket in closed_to_open:
                if stack and stack[-1] == closed_to_open[bracket]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(bracket)

        return True if not stack else False


# Implementation Steps:
# 1. Make a stack (list)
# 2. Create a hashmap with closing brackets as keys & opening as values
# 3. Run a loop over string
#   3.1 First check if the bracket is in hashmap (meaning if it's a closing bracket)?
#       3.1.1 If yes, then check if stack is NOT empty (meaning it has an opening bracket, doesn't matter whose)
#       3.1.2 AND if the last item of stack is opening bracket of that closing bracket (check from hashmap)
#           o If yes, then simply remove that last item (stack.pop)
#           o Else, return False
#   3.2 Else:
#       o Push the bracket in stack
# 4. Return true if stack is empty (meaning brackets in string were correctly placed)
