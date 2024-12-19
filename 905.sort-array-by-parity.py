#
# @lc app=leetcode id=905 lang=python
#
# [905] Sort Array By Parity
#

# @lc code=start
class Solution(object):
    def sortArrayByParity(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        left = 0

        for right in range(len(nums)):
            if nums[right] % 2 == 0:
                nums[left], nums[right] = nums[right], nums[left]
                left += 1

        return nums

        
# @lc code=end

