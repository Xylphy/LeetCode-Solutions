#
# @lc app=leetcode id=1913 lang=python
#
# [1913] Maximum Product Difference Between Two Pairs
#

# @lc code=start
class Solution(object):
    def maxProductDifference(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        return nums[-1] * nums[-2] - nums[0] * nums[1]
# @lc code=end

