#
# @lc app=leetcode id=200 lang=python
#
# [200] Number of Islands
#

# @lc code=start
class Solution(object):

    def bfs(self, grid, row, col, seen):
        queue = [(row, col)]

        while queue:
            row, col = queue.pop(0)
            
            if (row, col) in seen:
                continue

            seen.add((row, col))

            if row - 1 >= 0 and (row - 1, col) not in seen and grid[row - 1][col] == '1':
                queue.append((row - 1, col))
            if row + 1 < len(grid) and (row + 1, col) not in seen and grid[row + 1][col] == '1':
                queue.append((row + 1, col))
            if col - 1 >= 0 and (row, col - 1) not in seen and grid[row][col - 1] == '1':
                queue.append((row, col - 1))
            if col + 1 < len(grid[0]) and (row, col + 1) not in seen and grid[row][col + 1] == '1':
                queue.append((row, col + 1))


    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """

        islands = 0
        seen = set()

        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == '1' and (row, col) not in seen:
                    islands += 1
                    self.bfs(grid, row, col, seen)


        return islands
        
# @lc code=end

