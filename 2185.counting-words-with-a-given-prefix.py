#
# @lc app=leetcode id=2185 lang=python
#
# [2185] Counting Words With a Given Prefix
#

# @lc code=start
class Solution(object):
    def prefixCount(self, words, pref):
        """
        :type words: List[str]
        :type pref: str
        :rtype: int
        """
        count = 0
        for word in words:
            if word.startswith(pref):
                count += 1

        return count
        
# @lc code=end

