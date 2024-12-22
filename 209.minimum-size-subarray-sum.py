#
# @lc app=leetcode id=209 lang=python
#
# [209] Minimum Size Subarray Sum
#

# @lc code=start
class Solution(object):
    def minSubArrayLen(self, target, nums):
        """
        :type target: int
        :type nums: List[int]
        :rtype: int
        """
        min_len = float('inf')
        left = 0
        sum_nums = 0
        
        for right in range(len(nums)):
            sum_nums += nums[right]
            while sum_nums >= target:
                min_len = min(min_len, right - left + 1)
                sum_nums -= nums[left]
                left += 1

        return min_len if min_len != float('inf') else 0



        
# @lc code=end

