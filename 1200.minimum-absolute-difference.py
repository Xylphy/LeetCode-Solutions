#
# @lc app=leetcode id=1200 lang=python
#
# [1200] Minimum Absolute Difference
#

# @lc code=start
class Solution(object):
    def minimumAbsDifference(self, arr):
        """
        :type arr: List[int]
        :rtype: List[List[int]]
        """
        arr.sort()
        min_diff = float("inf")
        result = []

        for i in range(1, len(arr)):
            diff = arr[i] - arr[i - 1]
            if diff < min_diff:
                min_diff = diff
                result = [[arr[i - 1], arr[i]]]
            elif diff == min_diff:
                result.append([arr[i - 1], arr[i]])

        return result


# @lc code=end
