#
# @lc app=leetcode id=762 lang=python
#
# [762] Prime Number of Set Bits in Binary Representation
#

# @lc code=start
class Solution(object):
    def countPrimeSetBits(self, left, right):
        """
        :type left: int
        :type right: int
        :rtype: int
        """
        count = 0

        def countBits(n):
            count = 0
            while n:
                count += n & 1
                n >>= 1
            return count

        def isPrime(n):
            if n < 2:
                return False
            for i in range(2, int(n**0.5) + 1):
                if n % i == 0:
                    return False
            return True

        
        for i in range(left, right + 1):
            if isPrime(countBits(i)):
                count += 1

        return count
        
# @lc code=end

