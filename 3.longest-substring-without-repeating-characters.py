#
# @lc app=leetcode id=3 lang=python
#
# [3] Longest Substring Without Repeating Characters
#

# @lc code=start
class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        left = 0
        max_length = 0
        seen = {}

        for right in range(len(s)):
            if s[right] in seen:
                left = max(left, seen[s[right]] + 1)
            seen[s[right]] = right
            max_length = max(max_length, right - left + 1)
        
        return max_length
        
# @lc code=end

