#
# @lc app=leetcode id=1351 lang=python
#
# [1351] Count Negative Numbers in a Sorted Matrix
#

# @lc code=start
class Solution(object):
    def countNegatives(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """

        rows = len(grid)
        cols = len(grid[0]) if rows > 0 else 0
        r, c = 0, cols - 1
        count = 0
        while r < rows and c >= 0:
            if grid[r][c] < 0:
                count += rows - r
                c -= 1
            else:
                r += 1
        return count


# @lc code=end
