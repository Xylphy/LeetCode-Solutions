#
# @lc app=leetcode id=1758 lang=python
#
# [1758] Minimum Changes To Make Alternating Binary String
#

# @lc code=start
class Solution(object):
    def minOperations(self, s):
        """
        :type s: str
        :rtype: int
        """
        alt1 = 0 #0
        alt2 = 0 #1

        for i in range(len(s)):
            if i % 2 == 0:
                if s[i] == '0':
                    alt1 += 1
                else:
                    alt2 += 1
            else:
                if s[i] == '1':
                    alt1 += 1
                else:
                    alt2 += 1

        return min(alt1, alt2)

# @lc code=end

