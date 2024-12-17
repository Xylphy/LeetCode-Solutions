#
# @lc app=leetcode id=169 lang=python
#
# [169] Majority Element
#

# @lc code=start
class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        """ Boyer-Moore Voting Algorithm """

        count = 0
        candidate = None

        for i in nums:
            if count == 0:
                candidate = i
            count += 1 if i == candidate else -1

        return candidate
        
# @lc code=end