#
# @lc app=leetcode id=658 lang=python
#
# [658] Find K Closest Elements
#

# @lc code=start
class Solution(object):
    def findClosestElements(self, arr, k, x):
        """
        :type arr: List[int]
        :type k: int
        :type x: int
        :rtype: List[int]
        """
        sorted_arr = sorted(arr, key=lambda num: (abs(num - x), num))

        closest_elements = sorted_arr[:k]

        closest_elements.sort()

        return closest_elements
        
# @lc code=end

