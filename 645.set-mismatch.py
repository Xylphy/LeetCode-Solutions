#
# @lc app=leetcode id=645 lang=python
#
# [645] Set Mismatch
#

# @lc code=start
class Solution(object):
    def findErrorNums(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        missing = -1
        duplicate = -1

        for num in nums:
            if nums[abs(num) - 1] < 0:
                duplicate = abs(num)
            else:
                nums[abs(num) - 1] *= -1

        for i in range(len(nums)):
            if nums[i] > 0:
                missing = i + 1

        return [duplicate, missing]
        

        
        
# @lc code=end

