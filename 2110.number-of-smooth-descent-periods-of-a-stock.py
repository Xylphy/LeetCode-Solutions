#
# @lc app=leetcode id=2110 lang=python
#
# [2110] Number of Smooth Descent Periods of a Stock
#

# @lc code=start
class Solution(object):
    def getDescentPeriods(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        ans = 0
        ctr = 1

        for i in range(1, len(prices)):
            if prices[i] + 1 == prices[i - 1]:
                ctr += 1
            else:
                ans += (ctr * (ctr + 1)) // 2
                ctr = 1
        
        ans += (ctr * (ctr + 1)) // 2
        return ans
        
# @lc code=end

