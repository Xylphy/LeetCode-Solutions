#
# @lc app=leetcode id=414 lang=python
#
# [414] Third Maximum Number
#

# @lc code=start
class Solution(object):
    def thirdMax(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums = list(set(nums))

        if len(set(nums)) < 3:
            return max(nums)

        return sorted(nums)[-3]

        
        
        
        
        
# @lc code=end

