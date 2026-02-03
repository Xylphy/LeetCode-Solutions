#
# @lc app=leetcode id=1984 lang=python
#
# [1984] Minimum Difference Between Highest and Lowest of K Scores
#

# @lc code=start
class Solution(object):
    def minimumDifference(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        if k <= 1:
            return 0

        nums.sort()
        min_diff = float("inf")

        for i in range(len(nums) - k + 1):
            min_diff = min(min_diff, nums[i + k - 1] - nums[i])

        return min_diff


# @lc code=end
