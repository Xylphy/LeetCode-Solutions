#
# @lc app=leetcode id=949 lang=python
#
# [949] Largest Time for Given Digits
#


# @lc code=start


class Solution(object):
    def largestTimeFromDigits(self, arr):
        """
        :type arr: List[int]
        :rtype: str
        """

        import itertools

        best = -1

        for a, b, c, d in itertools.permutations(arr):
            h = a * 10 + b
            m = c * 10 + d

            if h < 24 and m < 60:
                t = h * 100 + m
                if t > best:
                    best = t

        return "" if best < 0 else "{:02}:{:02}".format(best // 100, best % 100)


# @lc code=end
