#
# @lc app=leetcode id=560 lang=python
#
# [560] Subarray Sum Equals K
#

# @lc code=start
class Solution(object):
    def subarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        prefix_sum = {0: 1}
        count = 0
        total_sum = 0

        for num in nums:
            count += num
            if count - k in prefix_sum:
                total_sum += prefix_sum[count - k]
            prefix_sum[count] = prefix_sum.get(count, 0) + 1
    
        return total_sum
        
# @lc code=end

