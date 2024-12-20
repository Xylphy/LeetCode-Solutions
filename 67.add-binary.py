#
# @lc app=leetcode id=67 lang=python
#
# [67] Add Binary
#

# @lc code=start
class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        carry = 0
        up = len(a) - 1
        down = len(b) - 1
        res = []

        while up >= 0 or down >= 0 or carry == 1:
            sum = carry
            if up >= 0:
                sum += int(a[up])
                up -= 1
            if down >= 0:
                sum += int(b[down])
                down -= 1

            carry, sum = divmod(sum, 2)
            res.append(str(sum))

        return ''.join(res[::-1])
        
# @lc code=end

