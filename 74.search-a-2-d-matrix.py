#
# @lc app=leetcode id=74 lang=python
#
# [74] Search a 2D Matrix
#


# @lc code=start
class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        left, right = 0, len(matrix) - 1
        mid = 0

        if not matrix or not matrix[0]:
            return False

        while left <= right:
            mid = (left + right) // 2
            if matrix[mid][0] <= target <= matrix[mid][-1]:
                break
            elif matrix[mid][0] > target:
                right = mid - 1
            else:
                left = mid + 1

        if left > right:
            return False

        row = mid

        left, right = 0, len(matrix[0]) - 1

        while left <= right:
            mid = (left + right) // 2
            if matrix[row][mid] == target:
                return True
            elif matrix[row][mid] < target:
                left = mid + 1
            else:
                right = mid - 1

        return False


# @lc code=end
