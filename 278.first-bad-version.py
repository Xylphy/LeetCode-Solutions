#
# @lc app=leetcode id=278 lang=python
#
# [278] First Bad Version
#

# @lc code=start
# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool
# def isBadVersion(version):

class Solution(object):
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        left = 1

        while left < n:
            middle = (left + n) // 2

            if isBadVersion(middle):
                n = middle
            else:
                left = middle + 1

        return left
            
        
# @lc code=end

