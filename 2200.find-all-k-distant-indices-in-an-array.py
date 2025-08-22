#
# @lc app=leetcode id=2200 lang=python
#
# [2200] Find All K-Distant Indices in an Array
#


# @lc code=start
class Solution(object):
    def findKDistantIndices(self, nums, key, k):
        """
        :type nums: List[int]
        :type key: int
        :type k: int
        :rtype: List[int]
        """
        key_indices = [i for i, num in enumerate(nums) if num == key]
        result = []
        
        j = 0
        for i in range(len(nums)):
            while j < len(key_indices) and key_indices[j] < i - k:
                j += 1
            if j < len(key_indices) and key_indices[j] <= i + k:
                result.append(i)

        return result
        


# @lc code=end
