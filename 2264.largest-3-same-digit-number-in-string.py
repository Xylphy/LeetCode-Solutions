#
# @lc app=leetcode id=2264 lang=python
#
# [2264] Largest 3-Same-Digit Number in String
#

# @lc code=start
class Solution(object):
    def largestGoodInteger(self, num):
        """
        :type num: str
        :rtype: str
        """
        max_num = ""
        for i in range(2, len(num)):
            if num[i] == num[i-1] == num[i-2]:
                max_num = max(max_num, num[i] * 3)

        return max_num
            
        
# @lc code=end

