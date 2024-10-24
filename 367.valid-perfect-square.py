#
# @lc app=leetcode id=367 lang=python
#
# [367] Valid Perfect Square
#

# @lc code=start
class Solution(object):
    def isPerfectSquare(self, num):
        """
        :type num: int
        :rtype: bool
        """
        left, right = 1, num

        while left <= right:
            middle = (left + right) // 2

            middle_square = middle * middle

            if middle_square == num:
                return True
            elif middle_square < num:
                left = middle + 1
            else:
                right = middle - 1

        return False

        
# @lc code=end

