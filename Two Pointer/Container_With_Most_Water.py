class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """

        temp = 0
        n = len(height)

        L = 0
        R = n - 1

        while L < R:
            width = R - L
            container_height = min(height[L], height[R])
            area = width * container_height

            temp = max(temp, area)

            if height[L] < height[R]:
                L += 1
            else:
                R -= 1

        return temp

        # result = 0

        # for i in range(len(height)):
        #     for j in range(i+1, len(height)):
        #         width = j - i
        #         container_height = min(height[i], height[j])
        #         area = width * container_height

        #         result = max(result, area)

        # return result
