#
# @lc app=leetcode id=2176 lang=python
#
# [2176] Count Equal and Divisible Pairs in an Array
#


# @lc code=start
class Solution(object):
    def countPairs(self, nums, k):
        from collections import defaultdict

        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        count = 0
        seen = defaultdict(list)

        for i, num in enumerate(nums):
            for j in seen[num]:
                if (i * j) % k == 0:
                    count += 1
            seen[num].append(i)

        return count


# @lc code=end
