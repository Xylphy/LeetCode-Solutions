#
# @lc app=leetcode id=647 lang=python
#
# [647] Palindromic Substrings
#

# @lc code=start
class Solution(object):
    def countSubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """
        n = len(s)
        dp_1 = [0] * n
        dp_2 = [0] * n

        dp_1[0] = 1


        for i in range(1, n):
            dp_2, dp_1 = dp_1, dp_2
            dp_1[i] = 1


            for j in range(i -1, -1, -1):
                if s[j] == s[i]:
                    dp_1









        
# @lc code=end

