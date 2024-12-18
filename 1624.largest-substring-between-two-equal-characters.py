#
# @lc app=leetcode id=1624 lang=python
#
# [1624] Largest Substring Between Two Equal Characters
#

# @lc code=start
class Solution(object):
    def maxLengthBetweenEqualCharacters(self, s):
        """
        :type s: str
        :rtype: int
        """
        max = -1
        map = {}

        for i in range(len(s)):
            if s[i] in map:
                if i - map[s[i]] - 1 > max:
                    max = i - map[s[i]] - 1
            else:
                map[s[i]] = i

        return max
            
        
# @lc code=end

