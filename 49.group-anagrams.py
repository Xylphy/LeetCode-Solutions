#
# @lc app=leetcode id=49 lang=python
#
# [49] Group Anagrams
#

# @lc code=start

class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        anagrams = {}

        for string in strs:
            sorted_string = tuple(sorted(string))

            if sorted_string in anagrams:
                anagrams[sorted_string].append(string)
            else:
                anagrams[sorted_string] = [string]

        return anagrams.values()


        
# @lc code=end

