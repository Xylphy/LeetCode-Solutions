#
# @lc app=leetcode id=2605 lang=python
#
# [2605] Form Smallest Number From Two Digit Arrays
#

# @lc code=start
class Solution(object):
    def minNumber(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: int
        """
        common = set(nums1) & set(nums2)

        if common:
            return min(common)

        min_num1 = min(nums1)
        min_num2 = min(nums2)

        return min(min_num1 * 10 + min_num2, min_num2 * 10 + min_num1)


# @lc code=end
