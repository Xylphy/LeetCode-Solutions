#
# @lc app=leetcode id=696 lang=python
#
# [696] Count Binary Substrings
#

# @lc code=start
class Solution(object):
    def countBinarySubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """

        count = 0
        prev_run_length = 0
        curr_run_length = 1

        for i in range(1, len(s)):
            if s[i] == s[i - 1]:
                curr_run_length += 1
            else:
                count += min(prev_run_length, curr_run_length)
                prev_run_length = curr_run_length
                curr_run_length = 1

        count += min(prev_run_length, curr_run_length)

        return count
        
# @lc code=end

