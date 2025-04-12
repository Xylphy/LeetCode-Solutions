#
# @lc app=leetcode id=37 lang=python
#
# [37] Sudoku Solver
#


# @lc code=start
class Solution(object):
    def solveSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: None Do not return anything, modify board in-place instead.
        """

        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        boxes = [set() for _ in range(9)]

        empty_cells = []
        for r in range(9):
            for c in range(9):
                if board[r][c] == ".":
                    empty_cells.append((r, c))
                else:
                    num = board[r][c]
                    rows[r].add(num)
                    cols[c].add(num)
                    boxes[(r // 3) * 3 + (c // 3)].add(num)

        def get_candidates(r, c):
            box_index = (r // 3) * 3 + (c // 3)
            return set("123456789") - rows[r] - cols[c] - boxes[box_index]

        def backtrack():
            if not empty_cells:
                return True

            empty_cells.sort(key=lambda x: len(get_candidates(*x)))
            r, c = empty_cells.pop(0)
            box_index = (r // 3) * 3 + (c // 3)

            for num in get_candidates(r, c):
                board[r][c] = num
                rows[r].add(num)
                cols[c].add(num)
                boxes[box_index].add(num)

                if backtrack():
                    return True

                board[r][c] = "."
                rows[r].remove(num)
                cols[c].remove(num)
                boxes[box_index].remove(num)

            empty_cells.insert(0, (r, c))
            return False

        backtrack()


# @lc code=end
