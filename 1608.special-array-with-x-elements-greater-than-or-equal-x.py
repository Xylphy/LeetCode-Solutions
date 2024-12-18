#
# @lc app=leetcode id=1608 lang=python
#
# [1608] Special Array With X Elements Greater Than or Equal X
#

# @lc code=start
class Solution(object):
    def specialArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        n = len(nums)
        for i in range(1, n + 1):
            if nums[n - i] >= i and (n - i == 0 or nums[n - i - 1] < i):
                return i

        return -1

        
# @lc code=end

