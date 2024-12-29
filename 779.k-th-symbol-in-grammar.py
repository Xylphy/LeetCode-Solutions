#
# @lc app=leetcode id=779 lang=python
#
# [779] K-th Symbol in Grammar
#

# @lc code=start
class Solution(object):
    def kthGrammar(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: int
        """
        if n == 1:
            return 0

        if k % 2 == 0:
            return 1 if self.kthGrammar(n - 1, k / 2) == 0 else 0
        else:
            return 0 if self.kthGrammar(n - 1, (k + 1) / 2) == 0 else 1
        
# @lc code=end

