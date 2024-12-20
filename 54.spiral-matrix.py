#
# @lc app=leetcode id=54 lang=python
#
# [54] Spiral Matrix
#

# @lc code=start
class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        up, right, down, left = 0, len(matrix[0]) - 1, len(matrix) - 1, 0
        res = []

        while up <= down and left <= right:
            for i in range(left, right + 1):
                res.append(matrix[up][i])
            up += 1

            for i in range(up, down + 1):
                res.append(matrix[i][right])
            right -= 1

            if up <= down:
                for i in range(right, left - 1, -1):
                    res.append(matrix[down][i])
                down -= 1

            if left <= right:
                for i in range(down, up - 1, -1):
                    res.append(matrix[i][left])
                left += 1

        return res
        
# @lc code=end

