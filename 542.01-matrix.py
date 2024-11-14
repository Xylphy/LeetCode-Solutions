#
# @lc app=leetcode id=542 lang=python
#
# [542] 01 Matrix
#

# @lc code=start
class Solution(object):
    def updateMatrix(self, mat):
        """
        :type mat: List[List[int]]
        :rtype: List[List[int]]
        """
        from collections import deque

        rows, cols = len(mat), len(mat[0])
        queue = deque()
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

        for r in range(rows):
            for c in range(cols):
                if mat[r][c] == 0:
                    queue.append((r, c))
                else:
                    mat[r][c] = float('inf')

        while queue:
            r, c = queue.popleft()
            for dr, dc in directions:
                new_r, new_c = r + dr, c + dc
                if 0 <= new_r < rows and 0 <= new_c < cols and mat[new_r][new_c] > mat[r][c] + 1:
                    mat[new_r][new_c] = mat[r][c] + 1
                    queue.append((new_r, new_c))

        return mat

        
                
        
# @lc code=end

