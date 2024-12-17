#
# @lc app=leetcode id=205 lang=python
#
# [205] Isomorphic Strings
#

# @lc code=start
class Solution(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """

        if len(s) != len(t):
            return False
        
        s_dict = {}

        for i in range(len(s)):
            if s[i] in s_dict:
                if s_dict[s[i]] != t[i]:
                    return False
            else:
                if t[i] in s_dict.values():
                    return False
                s_dict[s[i]] = t[i]

        return True

        
# @lc code=end

