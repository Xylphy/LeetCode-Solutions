#
# @lc app=leetcode id=27 lang=python
#
# [27] Remove Element
#

# @lc code=start
class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        tmp = []

        for i in range(len(nums)):
            if nums[i] != val:
                tmp.append(nums[i])

        for i in range(len(tmp)):
            nums[i] = tmp[i]

        return len(tmp)
        
# @lc code=end

