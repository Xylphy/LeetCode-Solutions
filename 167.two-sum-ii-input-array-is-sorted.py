#
# @lc app=leetcode id=167 lang=python
#
# [167] Two Sum II - Input Array Is Sorted
#

# @lc code=start
class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        left, right = 0, len(numbers) - 1
        while numbers[left] + numbers[right] != target:
            if numbers[left] + numbers[right] < target:
                left += 1
            else:
                right -= 1

        return [left + 1, right + 1]

        
# @lc code=end

