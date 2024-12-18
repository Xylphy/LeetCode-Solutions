#
# @lc app=leetcode id=36 lang=python
#
# [36] Valid Sudoku
#

# @lc code=start
class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        loc_cells = set()
        board_loc = set()

        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] != '.':
                    cur = board[i][j]
                    if (i, cur) in loc_cells or (cur, j) in loc_cells or (i // 3, j // 3, cur) in board_loc:
                        return False
                    loc_cells.add((i, cur))
                    loc_cells.add((cur, j))
                    board_loc.add((i // 3, j // 3, cur))

        return True

        
# @lc code=end

