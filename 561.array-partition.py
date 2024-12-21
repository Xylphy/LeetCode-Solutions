#
# @lc app=leetcode id=561 lang=python
#
# [561] Array Partition
#

# @lc code=start
class Solution(object):
    def arrayPairSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        return sum(sorted(nums)[::2])

        
# @lc code=end

