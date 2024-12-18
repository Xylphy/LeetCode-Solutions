#
# @lc app=leetcode id=128 lang=python
#
# [128] Longest Consecutive Sequence
#

# @lc code=start
class Solution():

    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        set_nums = set(nums)
        max_length = 0

        for num in set_nums:
            if num - 1 not in set_nums:
                current_num = num
                current_length = 1

                while current_num + 1 in set_nums:
                    current_num += 1
                    current_length += 1

                max_length = max(max_length, current_length)

        return max_length
        
# @lc code=end

