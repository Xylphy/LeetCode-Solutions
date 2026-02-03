#
# @lc app=leetcode id=516 lang=python
#
# [516] Longest Palindromic Subsequence
#

# @lc code=start
class Solution(object):
    def longestPalindromeSubseq(self, s):
        """
        :type s: str
        :rtype: int
        """
        dp_1 = [0] * len(s)
        dp_2 = [0] * len(s)

        dp_1[0] = 1

        for i in range(1, len(s)):
            dp_2, dp_1 = dp_1, dp_2
            dp_1[i] = 1

            for j in range(i - 1, -1, -1):
                if s[i] == s[j]:
                    dp_1[j] = dp_2[j + 1] + 2
                else:
                    dp_1[j] = max(dp_1[j + 1], dp_2[j])

        return dp_1[0]


# @lc code=end
