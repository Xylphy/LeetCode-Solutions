#
# @lc app=leetcode id=1267 lang=python
#
# [1267] Count Servers that Communicate
#


# @lc code=start
class Solution(object):
    def countServers(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        res = 0

        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == 1:
                    partial_res = 0

                    for i in range(0, len(grid)):
                        if grid[i][col] == 1 and i != row:
                            partial_res += 1
                            break

                    for i in range(0, len(grid[0])):
                        if grid[row][i] == 1 and i != col:
                            partial_res += 1
                            break

                    if partial_res > 0:
                        res += 1

        return res


# @lc code=end
