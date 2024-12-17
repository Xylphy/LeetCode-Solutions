#
# @lc app=leetcode id=1512 lang=python
#
# [1512] Number of Good Pairs
#

# @lc code=start
class Solution(object):
    def numIdenticalPairs(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        frequency = {}
        max = 0
        for num in nums:
            if num in frequency:
                frequency[num] += 1
                max += frequency[num]
            else:
                frequency[num] = 0

        return max
        
# @lc code=end

