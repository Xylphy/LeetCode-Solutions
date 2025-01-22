#
# @lc app=leetcode id=1765 lang=python
#
# [1765] Map of Highest Peak
#

# @lc code=start
class Solution(object):
    def highestPeak(self, isWater):
        """
        :type isWater: List[List[int]]
        :rtype: List[List[int]]
        """
        from collections import deque

        queue = deque()
        m, n = len(isWater), len(isWater[0])
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

        for i in range(m):
            for j in range(n):
                if isWater[i][j] == 1:
                    isWater[i][j] = 0
                    queue.append((i, j))
                else:
                    isWater[i][j] = float('inf')

        while queue:
            i, j = queue.popleft()
            
            for dx, dy in directions:
                new_x, new_y = i + dx, j + dy
                if 0 <= new_x < m and 0 <= new_y < n and isWater[new_x][new_y] > isWater[i][j] + 1:
                    isWater[new_x][new_y] = isWater[i][j] + 1
                    queue.append((new_x, new_y))

        return isWater
        
# @lc code=end

