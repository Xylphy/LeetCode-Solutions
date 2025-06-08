#
# @lc app=leetcode id=386 lang=python
#
# [386] Lexicographical Numbers
#


# @lc code=start
class Solution(object):
    def lexicalOrder(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        result = []

        def dfs(num):
            if num > n:
                return
            result.append(num)
            for i in range(10):
                next_num = num * 10 + i
                if next_num <= n:
                    dfs(next_num)

        for i in range(1, 10):
            dfs(i)

        return result


# @lc code=end
