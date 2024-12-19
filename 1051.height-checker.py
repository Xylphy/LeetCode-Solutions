#
# @lc app=leetcode id=1051 lang=python
#
# [1051] Height Checker
#

# @lc code=start
class Solution(object):
    def heightChecker(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """
        sorted_heights = sorted(heights)

        res = 0
        for i in range(len(heights)):
            if heights[i] != sorted_heights[i]:
                res += 1

        return res
        
# @lc code=end

