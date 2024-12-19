#
# @lc app=leetcode id=412 lang=python
#
# [412] Fizz Buzz
#

# @lc code=start
class Solution(object):
    def fizzBuzz(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        return [str(i) if (i % 3 != 0 and i % 5 != 0) else "Fizz" if i % 3 == 0 and i % 5 != 0 else "Buzz" if i % 3 != 0 and i % 5 == 0 else "FizzBuzz" for i in range(1, n + 1)]
        
# @lc code=end

