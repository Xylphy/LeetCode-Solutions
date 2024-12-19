#
# @lc app=leetcode id=941 lang=python
#
# [941] Valid Mountain Array
#

# @lc code=start
class Solution(object):
    def validMountainArray(self, arr):
        """
        :type arr: List[int]
        :rtype: bool
        """
        if len(arr) < 3:
            return False

        i = 0

        while i + 1 < len(arr) and arr[i] < arr[i + 1]:
            i += 1

        if i == 0 or i == len(arr) - 1:
            return False
        
        while i + 1 < len(arr) and arr[i] > arr[i + 1]:
            i += 1

        return i == len(arr) - 1
        
# @lc code=end

