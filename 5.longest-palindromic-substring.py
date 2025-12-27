#
# @lc app=leetcode id=5 lang=python
#
# [5] Longest Palindromic Substring
#

# @lc code=start



class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """

        n = len(s)

        dp = [[True] * n for _ in range(n)]

        start_pos = 0
        max_len = 1

        for i in range(n - 2, -1, -1):
            for j in range(i + 1, n):
                dp[i][j] = False

                if s[i] == s[j]:
                    dp[i][j] = dp[i + 1][j - 1]

                    if dp[i][j] and max_len < j - i + 1:
                        max_len = j - i + 1
                        start_pos = i

        return s[start_pos : start_pos + max_len]


# @lc code=end
