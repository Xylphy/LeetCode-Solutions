#
# @lc app=leetcode id=52 lang=python
#
# [52] N-Queens II
#


# @lc code=start
class Solution(object):
    def totalNQueens(self, n):
        """
        :type n: int
        :rtype: int
        """

        def backtrack(row, cols, pos_diags, neg_diags):
            if row == n:
                return 1

            count = 0
            available_positions = (~(cols | pos_diags | neg_diags)) & ((1 << n) - 1)

            while available_positions:
                position = available_positions & -available_positions
                available_positions &= available_positions - 1

                count += backtrack(
                    row + 1,
                    cols | position,
                    (pos_diags | position) << 1,
                    (neg_diags | position) >> 1,
                )

            return count

        return backtrack(0, 0, 0, 0)


# @lc code=end
