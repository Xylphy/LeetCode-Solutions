#
# @lc app=leetcode id=118 lang=python
#
# [118] Pascal's Triangle
#

# @lc code=start
class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        result = []

        for i in range(numRows):
            if i == 0:
                result = [[1]]
            else:
                result.append([1] + [result[i - 1][j] + result[i - 1][j + 1] for j in range(len(result[i - 1]) - 1)] + [1])

        return result
        
# @lc code=end

