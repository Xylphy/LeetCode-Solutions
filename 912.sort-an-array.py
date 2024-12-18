#
# @lc app=leetcode id=912 lang=python
#
# [912] Sort an Array
#

# @lc code=start
class Solution(object):
    def merge(self, left, right):
        i, j = 0, 0
        result = []
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                result.append(left[i])
                i += 1
            else:
                result.append(right[j])
                j += 1

        result += left[i:]
        result += right[j:]

        return result

    def mergeSort(self, nums):
        if len(nums) <= 1:
            return nums
        mid = len(nums) // 2

        left = self.mergeSort(nums[:mid])
        right = self.mergeSort(nums[mid:])

        return self.merge(left, right)

    def sortArray(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        return self.mergeSort(nums)

        
# @lc code=end

