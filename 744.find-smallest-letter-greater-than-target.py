#
# @lc app=leetcode id=744 lang=python
#
# [744] Find Smallest Letter Greater Than Target
#


# @lc code=start
class Solution(object):
    def nextGreatestLetter(self, letters, target):
        """
        :type letters: List[str]
        :type target: str
        :rtype: str
        """
        left, right = 0, len(letters) - 1

        while left < right:
            middle = (left + right) // 2

            if ord(letters[middle]) <= ord(target):
                left = middle + 1
            else:
                right = middle

        return letters[left] if ord(letters[left]) > ord(target) else letters[0]


# @lc code=end
