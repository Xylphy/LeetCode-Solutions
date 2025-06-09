#
# @lc app=leetcode id=440 lang=python
#
# [440] K-th Smallest in Lexicographical Order
#


# @lc code=start
class Solution(object):
    def findKthNumber(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: int
        """

        def count_steps(prefix, n):
            cur = prefix
            next_prefix = prefix + 1
            steps = 0

            while cur <= n:
                steps += min(n + 1, next_prefix) - cur
                cur *= 10
                next_prefix *= 10

            return steps

        prefix = 1
        k -= 1
        while k > 0:
            steps = count_steps(prefix, n)

            if steps <= k:
                prefix += 1
                k -= steps
            else:
                prefix *= 10
                k -= 1

        return prefix


# @lc code=end
