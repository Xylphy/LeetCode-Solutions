#
# @lc app=leetcode id=769 lang=python
#
# [769] Max Chunks To Make Sorted
#

# @lc code=start
class Solution(object):
    def maxChunksToSorted(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        current_sum = 0
        expected_num = 0
        chunks = 0

        for i, num in enumerate(arr):
            current_sum += num
            expected_num += i
            if current_sum == expected_num:
                chunks += 1

        return chunks

        
# @lc code=end

