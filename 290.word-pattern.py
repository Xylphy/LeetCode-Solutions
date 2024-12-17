#
# @lc app=leetcode id=290 lang=python
#
# [290] Word Pattern
#

# @lc code=start
class Solution(object):
    def wordPattern(self, pattern, s):
        """
        :type pattern: str
        :type s: str
        :rtype: bool
        """
        pattern_dict = {}
        splitted = s.split(" ")

        if len(pattern) != len(splitted):
            return False

        for c in range(len(pattern)):
            if pattern[c] in pattern_dict:
                if pattern_dict[pattern[c]] != splitted[c]:
                    return False
            else:
                if splitted[c] in pattern_dict.values():
                    return False
                pattern_dict[pattern[c]] = splitted[c]

        return True
        
# @lc code=end

