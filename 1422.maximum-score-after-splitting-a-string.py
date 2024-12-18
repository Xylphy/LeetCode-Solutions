#
# @lc app=leetcode id=1422 lang=python
#
# [1422] Maximum Score After Splitting a String
#

# @lc code=start
class Solution(object):
    def maxScore(self, s):
        """
        :type s: str
        :rtype: int
        """
        total_ones = 0

        for i in s:
            if i == '1':
                total_ones += 1
        
        total_zeros = 0

        res = 0

        for i in range(1, len(s)):
            if s[i - 1] == '0':
                total_zeros += 1
            else:
                total_ones -= 1

            res = max(res, total_zeros + total_ones)

        return res


        
# @lc code=end

