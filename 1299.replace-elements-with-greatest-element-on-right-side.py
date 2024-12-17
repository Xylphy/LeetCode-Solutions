#
# @lc app=leetcode id=1299 lang=python
#
# [1299] Replace Elements with Greatest Element on Right Side
#

# @lc code=start
class Solution(object):
    def replaceElements(self, arr):
        """
        :type arr: List[int]
        :rtype: List[int]
        """
        max = arr[-1]
        arr[-1] = -1

        for i in range(len(arr) - 2, -1, -1):
            current_max = arr[i]
            arr[i] = max
            if current_max > max:
                max = current_max

        return arr
                






        
        
# @lc code=end

