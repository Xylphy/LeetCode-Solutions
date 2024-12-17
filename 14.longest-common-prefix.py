#
# @lc app=leetcode id=14 lang=python
#
# [14] Longest Common Prefix
#

# @lc code=start
class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        string = ""
        index = 0;
        while True:
            try:
                for i in range(1, len(strs)):
                    if strs[i][index] != strs[0][index]:
                        return string
                string += strs[0][index]
                index += 1
            except:
                return string
        
        
# @lc code=end

