#
# @lc app=leetcode id=350 lang=python
#
# [350] Intersection of Two Arrays II
#

# @lc code=start
class Solution(object):
    def intersect(self, nums1, nums2):
        from collections import Counter
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        counter_nums1 = Counter(nums1)
        counter_num2 = Counter(nums2)

        result = []

        for key, value in counter_nums1.items():
            if key in counter_num2:
                result.extend([key] * min(value, counter_num2[key]))

        return result

        
# @lc code=end

