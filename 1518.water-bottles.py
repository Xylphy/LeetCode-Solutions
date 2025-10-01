#
# @lc app=leetcode id=1518 lang=python
#
# [1518] Water Bottles
#


# @lc code=start
class Solution(object):
    def numWaterBottles(self, numBottles, numExchange):
        """
        :type numBottles: int
        :type numExchange: int
        :rtype: int
        """
        return numBottles + (numBottles - 1) // (numExchange - 1)


# @lc code=end
