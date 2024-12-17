#
# @lc app=leetcode id=1189 lang=python
#
# [1189] Maximum Number of Balloons
#

# @lc code=start
class Solution(object):
    def maxNumberOfBalloons(self, text):
        from collections import Counter
        """
        :type text: str
        :rtype: int
        """
        count = Counter(text)
        return min(count['b'], count['a'], count['l'] // 2, count['o'] // 2, count['n'])
        
# @lc code=end

