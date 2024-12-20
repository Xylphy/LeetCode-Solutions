#
# @lc app=leetcode id=66 lang=python
#
# [66] Plus One
#

# @lc code=start
class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        index = len(digits) - 1
        carry = 1

        while carry == 1:
            if index < 0:
                return [1] + digits

            carry, digits[index] = divmod(digits[index] + carry, 10)
            index -= 1

        return digits
        
# @lc code=end

