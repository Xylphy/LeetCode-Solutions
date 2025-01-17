#
# @lc app=leetcode id=494 lang=python
#
# [494] Target Sum
#


# @lc code=start
class Solution(object):
    def findTargetSumWays(self, nums, target):
        from collections import deque
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        index = len(nums) - 1
        curr_sum = 0
        memo = {}

        def dfs(index, curr_sum):
            if index < 0:
                if curr_sum == target:
                    return 1
                return 0

            if (index, curr_sum) in memo:
                return memo[(index, curr_sum)]

            positive = dfs(index - 1, curr_sum + nums[index])
            negative = dfs(index - 1, curr_sum - nums[index])

            memo[(index, curr_sum)] = positive + negative
            return memo[(index, curr_sum)]

        return dfs(index, curr_sum)


# @lc code=end
