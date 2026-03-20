#
# @lc app=leetcode id=1594 lang=python
#
# [1594] Maximum Non Negative Product in a Matrix
#

# @lc code=start
class Solution(object):
    def maxProductPath(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        MOD = 10**9 + 7
        n = len(grid)
        m = len(grid[0])

        max_dp = [[0] * m for _ in range(n)]
        min_dp = [[0] * m for _ in range(n)]

        max_dp[0][0] = min_dp[0][0] = grid[0][0]

        for i in range(n):
            for j in range(m):
                if i == 0 and j == 0:
                    continue
                val = grid[i][j]
                candidates = []
                if i > 0:
                    candidates.append(val * max_dp[i - 1][j])
                    candidates.append(val * min_dp[i - 1][j])
                if j > 0:
                    candidates.append(val * max_dp[i][j - 1])
                    candidates.append(val * min_dp[i][j - 1])

                max_dp[i][j] = max(candidates)
                min_dp[i][j] = min(candidates)

        result = max_dp[-1][-1]
        if result < 0:
            return -1
        return result % MOD


# @lc code=end
