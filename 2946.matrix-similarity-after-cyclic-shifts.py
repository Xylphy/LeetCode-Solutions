#
# @lc app=leetcode id=2946 lang=python
#
# [2946] Matrix Similarity After Cyclic Shifts
#

# @lc code=start
class Solution(object):
    def areSimilar(self, mat, k):
        """
        :type mat: List[List[int]]
        :type k: int
        :rtype: bool
        """
        m = len(mat[0])

        k %= m
        if k == 0:
            return True

        for i, row in enumerate(mat):
            if (i & 1) == 0 and row != row[-k:] + row[:-k] or row != row[k:] + row[:k]:
                    return False
        return True


# @lc code=end
