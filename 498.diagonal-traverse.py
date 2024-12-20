#
# @lc app=leetcode id=498 lang=python
#
# [498] Diagonal Traverse
#

# @lc code=start
class Solution(object):
    def findDiagonalOrder(self, mat):
        """
        :type mat: List[List[int]]
        :rtype: List[int]
        """
        if not mat:
            return []
        
        m, n = len(mat), len(mat[0])
        res = []
        i, j = 0, 0
        for _ in range(m * n):
            res.append(mat[i][j])
            if (i + j) % 2 == 0:
                if j == n - 1:
                    i += 1
                elif i == 0:
                    j += 1
                else:
                    i -= 1
                    j += 1
            else:
                if i == m - 1:
                    j += 1
                elif j == 0:
                    i += 1
                else:
                    i += 1
                    j -= 1
            
        return res


        
# @lc code=end

