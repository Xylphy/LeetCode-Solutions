#
# @lc app=leetcode id=1897 lang=python
#
# [1897] Redistribute Characters to Make All Strings Equal
#

# @lc code=start
class Solution(object):
    def makeEqual(self, words):
        """
        :type words: List[str]
        :rtype: bool
        """
        frequency = {}
        for word in words:
            for char in word:
                if char in frequency:
                    frequency[char] += 1
                else:
                    frequency[char] = 1

        return all([v % len(words) == 0 for v in frequency.values()])
        
# @lc code=end

