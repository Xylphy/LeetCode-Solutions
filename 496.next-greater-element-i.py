#
# @lc app=leetcode id=496 lang=python
#
# [496] Next Greater Element I
#

# @lc code=start
class Solution(object):
    def nextGreaterElement(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """

        next_greater = {}
        stack = []

        for i in nums2:
            while stack and stack[-1] < i:
                next_greater[stack.pop()] = i
            stack.append(i)

        return [next_greater.get(i, -1) for i in nums1]


# @lc code=end
