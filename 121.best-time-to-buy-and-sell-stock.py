#
# @lc app=leetcode id=121 lang=python
#
# [121] Best Time to Buy and Sell Stock
#

# @lc code=start
class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        low, high = float('inf'), 0
        for price in prices:
            low = min(low, price)
            high = max(high, price - low)

        return high
        
# @lc code=end

