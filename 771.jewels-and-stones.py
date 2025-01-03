#
# @lc app=leetcode id=771 lang=python
#
# [771] Jewels and Stones
#

# @lc code=start
class Solution(object):
    def numJewelsInStones(self, jewels, stones):
        """
        :type jewels: str
        :type stones: str
        :rtype: int
        """
        set_jewels = set(jewels)
        count = 0

        for stone in stones:
            if stone in set_jewels:
                count += 1

        return count
        
# @lc code=end

