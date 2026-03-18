#
# @lc app=leetcode id=84 lang=python
#
# [84] Largest Rectangle in Histogram
#

# @lc code=start


class Solution(object):
    def largestRectangleArea(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """
        stack = []
        max_area = 0
        for i in range(len(heights) + 1):
            while stack and (i == len(heights) or heights[stack[-1]] >= heights[i]):
                height = heights[stack.pop()]
                width = i if not stack else i - stack[-1] - 1
                max_area = max(max_area, height * width)
            stack.append(i)
        return max_area

        
# @lc code=end

