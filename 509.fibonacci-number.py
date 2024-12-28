#
# @lc app=leetcode id=509 lang=python
#
# [509] Fibonacci Number
#

# @lc code=start
class Solution(object):
    def fib(self, n):
        """
        :type n: int
        :rtype: int
        """
        
        def fib_memo(n, memo):
            if n in memo:
                return memo[n]
            if n <= 1:
                return n

            memo[n] = fib_memo(n - 1, memo) + fib_memo(n - 2, memo)

            return memo[n]

        return fib_memo(n, {})
        
# @lc code=end

