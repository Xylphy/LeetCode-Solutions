#
# @lc app=leetcode id=242 lang=python
#
# [242] Valid Anagram
#

# @lc code=start
class Solution(object):
    def isAnagram(self, s, t):
        from collections import Counter
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        
        return Counter(s) == Counter(t)

# @lc code=end
