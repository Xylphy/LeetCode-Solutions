#
# @lc app=leetcode id=1295 lang=python
#
# [1295] Find Numbers with Even Number of Digits
#

# @lc code=start
class Solution(object):
    def findNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        return len([num for num in nums if len(str(num)) % 2 == 0])
        
# @lc code=end

