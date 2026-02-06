#
# @lc app=leetcode id=2078 lang=python
#
# [2078] Two Furthest Houses With Different Colors
#

# @lc code=start
class Solution(object):
    def maxDistance(self, colors):
        """
        :type colors: List[int]
        :rtype: int
        """

        n = len(colors)

        for i in range(n, -1, -1):
            if colors[0] != colors[i - 1]:
                return i - 1
            elif colors[n - 1] != colors[n - i]:
                return i - 1

        return 0
        
# @lc code=end

