#
# @lc app=leetcode id=1089 lang=python
#
# [1089] Duplicate Zeros
#

# @lc code=start
class Solution(object):
    def duplicateZeros(self, arr):
        """
        :type arr: List[int]
        :rtype: None Do not return anything, modify arr in-place instead.
        """
        dummy = []
        for num in arr:
            if num == 0:
                dummy.append(0)
            dummy.append(num)

        for i in range(len(arr)):
            arr[i] = dummy[i]
        
# @lc code=end

