#
# @lc app=leetcode id=51 lang=python
#
# [51] N-Queens
#


# @lc code=start
class Solution(object):
    def solveNQueens(self, n):
        """
        :type n: int
        :rtype: List[List[str]]
        """

        solutions = []
        cols = set()
        diags = set()
        anti_dags = set()
        board = [["."] * n for _ in range(n)]

        def solve(row):
            if row == n:
                solutions.append(["".join(r) for r in board])
                return

            for col in range(n):
                if col in cols or (row - col) in diags or (row + col) in anti_dags:
                    continue

                board[row][col] = "Q"
                cols.add(col)
                diags.add(row - col)
                anti_dags.add(row + col)

                solve(row + 1)

                board[row][col] = "."
                cols.remove(col)
                diags.remove(row - col)
                anti_dags.remove(row + col)

        solve(0)

        return solutions


# @lc code=end
