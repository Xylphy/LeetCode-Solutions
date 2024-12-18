#
# @lc app=leetcode id=238 lang=python
#
# [238] Product of Array Except Self
#

# @lc code=start
class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        length = len(nums)
        result = [1] * length

        left_product = 1
        for i in range(length):
            result[i] = left_product
            left_product *= nums[i]
        
        right_product = 1
        for i in range(length - 1, -1, -1):
            result[i] *= right_product
            right_product *= nums[i]

        return result
            


        
# @lc code=end

