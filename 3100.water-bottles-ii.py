#
# @lc app=leetcode id=3100 lang=python3
#
# [3100] Water Bottles II
#

# @lc code=start


class Solution:
    def maxBottlesDrunk(self, numBottles: int, numExchange: int) -> int:
        b = 2 * numExchange - 3
        return numBottles + int((-b + (b**2 + 4 * 2 * (numBottles - 1)) ** 0.5) // 2)


# @lc code=end
