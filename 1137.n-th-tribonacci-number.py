#
# @lc app=leetcode id=1137 lang=python
#
# [1137] N-th Tribonacci Number
#

# @lc code=start
class Solution(object):
    def tribonacci(self, n):
        """
        :type n: int
        :rtype: int
        """

        memo = {0: 0, 1: 1, 2: 1}

        def dp(n):
            if n in memo:
                return memo[n]

            memo[n] = dp(n - 1) + dp(n - 2) + dp(n - 3)
            return memo[n]

        return dp(n)


# @lc code=end
