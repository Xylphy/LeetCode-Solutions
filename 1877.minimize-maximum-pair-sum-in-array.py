#
# @lc app=leetcode id=1877 lang=python
#
# [1877] Minimize Maximum Pair Sum in Array
#

# @lc code=start
class Solution(object):
    def minPairSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        max_pair_sum = 0
        left, right = 0, len(nums) - 1

        while left < right:
            pair_sum = nums[left] + nums[right]
            max_pair_sum = max(max_pair_sum, pair_sum)
            left += 1
            right -= 1

        return max_pair_sum
        
# @lc code=end

