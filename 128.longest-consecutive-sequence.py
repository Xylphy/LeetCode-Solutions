#
# @lc app=leetcode id=128 lang=python
#
# [128] Longest Consecutive Sequence
#

# @lc code=start
class Solution():
    def union_find(self, union_find, num1):
        while num1 in union_find:
            if union_find[num1] is None:
                return num1
            num1 = union_find[num1]


    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        union_find = {}
        frequency = {}

        for num in nums:
            if num not in union_find:
                union_find[num] = None
                frequency[num] = 1

                union_find_left = self.union_find(union_find, num - 1)
                union_find_right = self.union_find(union_find, num + 1)

                if union_find_left is not None:
                    frequency[num] += frequency[union_find_left]
                    union_find[union_find_left] = num

                if union_find_right is not None:
                    frequency[num] += frequency[union_find_right]
                    union_find[union_find_right] = num

        return max(frequency.values() or [0])
        
# @lc code=end

