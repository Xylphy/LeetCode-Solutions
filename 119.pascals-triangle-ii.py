#
# @lc app=leetcode id=119 lang=python
#
# [119] Pascal's Triangle II
#

# @lc code=start
class Solution(object):
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        row_triangle = [1] * (rowIndex + 1)

        for i in range(1, rowIndex):
            for j in range(i, 0, -1):
                row_triangle[j] += row_triangle[j - 1]

        return row_triangle
            
        
# @lc code=end

