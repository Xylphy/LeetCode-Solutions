#
# @lc app=leetcode id=374 lang=python
#
# [374] Guess Number Higher or Lower
#

# @lc code=start
# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num):

class Solution(object):
    def guessNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        left, right = 0, n
        while left < right:
            mid = left + (right - left) // 2
            if guess(mid) == 0:
                return mid
            elif guess(mid) == -1:
                right = mid
            else:
                left = mid + 1

        return left
        
# @lc code=end

