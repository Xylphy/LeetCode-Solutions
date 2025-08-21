#
# @lc app=leetcode id=4 lang=python
#
# [4] Median of Two Sorted Arrays
#


# @lc code=start
class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """

        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1
        
        m, n = len(nums1), len(nums2)
        total_length = m + n
        
        if m == 0:
            if n % 2 == 0:
                return (nums2[n//2 - 1] + nums2[n//2]) / 2.0
            else:
                return nums2[n//2]
        

        left, right = 0, m
        while left <= right:
            partition1 = (left + right) // 2
            partition2 = (total_length + 1) // 2 - partition1
            
            nums1_left_max = float("-inf") if partition1 == 0 else nums1[partition1 - 1]
            nums1_right_min = float("inf") if partition1 == m else nums1[partition1]
            nums2_left_max = float("-inf") if partition2 == 0 else nums2[partition2 - 1]
            nums2_right_min = float("inf") if partition2 == n else nums2[partition2]
            
            if nums1_left_max <= nums2_right_min and nums2_left_max <= nums1_right_min:
                if total_length % 2 == 0:
                    return (max(nums1_left_max, nums2_left_max) + min(nums1_right_min, nums2_right_min)) / 2.0
                else:
                    return max(nums1_left_max, nums2_left_max)
            
            elif nums1_left_max > nums2_right_min:
                right = partition1 - 1
            else:
                left = partition1 + 1
        
        raise -1


# @lc code=end
