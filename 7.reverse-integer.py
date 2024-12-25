#
# @lc app=leetcode id=7 lang=python
#
# [7] Reverse Integer
#

# @lc code=start
class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        dup = int(str(abs(x))[::-1])
        if x < 0:
            dup = -dup

        return dup if -2**31 <= dup <= 2**31 - 1 else 0

        

        
# @lc code=end

