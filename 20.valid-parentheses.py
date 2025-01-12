#
# @lc app=leetcode id=20 lang=python
#
# [20] Valid Parentheses
#


# @lc code=start
class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = []

        for c in s:
            if c == "{" or c == "[" or c == "(":
                stack.append(c)
            else:
                if not stack:
                    return False
                if (
                    c == "}"
                    and stack[-1] != "{"
                    or c == "]"
                    and stack[-1] != "["
                    or c == ")"
                    and stack[-1] != "("
                ):
                    return False

                stack.pop()

        return not stack


# @lc code=end
