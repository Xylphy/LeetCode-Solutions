#
# @lc app=leetcode id=747 lang=python
#
# [747] Largest Number At Least Twice of Others
#

# @lc code=start
class Solution(object):
    def dominantIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        second_max = first_max = float('-inf')
        max_index = -1

        for i in range(len(nums)):
            if nums[i] > first_max:
                second_max, first_max = first_max, nums[i]
                max_index = i
            elif nums[i] > second_max:
                second_max = nums[i]

        return max_index if first_max >= 2 * second_max else -1
            
        
        
# @lc code=end

