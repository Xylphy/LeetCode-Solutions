#
# @lc app=leetcode id=1475 lang=python
#
# [1475] Final Prices With a Special Discount in a Shop
#

# @lc code=start
class Solution(object):
    def finalPrices(self, prices):
        """
        :type prices: List[int]
        :rtype: List[int]
        """
        stack = []
        for i, price in enumerate(prices):
            while stack and prices[stack[-1]] >= price:
                prices[stack.pop()] -= price
            stack.append(i)
        return prices
        
# @lc code=end

