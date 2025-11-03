#
# @lc app=leetcode id=79 lang=python
#
# [79] Word Search
#


# @lc code=start
class Solution(object):
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """

        def dfs(i, j, k):
            if (
                not 0 <= i < len(board)
                or not 0 <= j < len(board[0])
                or board[i][j] != word[k]
            ):
                return False
            if k == len(word) - 1:
                return True

            temp, board[i][j] = board[i][j], "/"
            found = (
                dfs(i + 1, j, k + 1)
                or dfs(i - 1, j, k + 1)
                or dfs(i, j + 1, k + 1)
                or dfs(i, j - 1, k + 1)
            )
            board[i][j] = temp
            return found

        for i in range(len(board)):
            for j in range(len(board[0])):
                if dfs(i, j, 0):
                    return True
        return False


# @lc code=end
