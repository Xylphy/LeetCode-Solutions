#
# @lc app=leetcode id=746 lang=python
#
# [746] Min Cost Climbing Stairs
#

# @lc code=start
class Solution(object):
    def minCostClimbingStairs(self, cost):
        """
        :type cost: List[int]
        :rtype: int
        """
        tabulation = [0] * (len(cost) + 1)

        for i in range(2, len(cost) + 1):
            tabulation[i] = min(
                tabulation[i - 1] + cost[i - 1], tabulation[i - 2] + cost[i - 2]
            )
        return tabulation[-1]


# @lc code=end
