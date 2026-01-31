#
# @lc app=leetcode id=3784 lang=python
#
# [3784] Minimum Deletion Cost to Make All Characters Equal
#

# @lc code=start


class Solution(object):
    def minCost(self, s, cost):
        """
        :type s: str
        :type cost: List[int]
        :rtype: int
        """
        total = sum(cost)
        keep = {}

        for ch, c in zip(s, cost):
            keep[ch] = keep.get(ch, 0) + c

        return total - max(keep.values())

# @lc code=end
