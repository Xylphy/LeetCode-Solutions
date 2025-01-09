#
# @lc app=leetcode id=279 lang=python
#
# [279] Perfect Squares
#

# @lc code=start
class Solution(object):
    def numSquares(self, n):
        from collections import deque
        """
        :type n: int
        :rtype: int
        """
        queue = deque([n])
        level = 0
        seen = set()

        if int(n ** 0.5) ** 2 == n:
            return 1

        while queue:
            level += 1
            for _ in range(len(queue)):
                num = queue.popleft()

                for i in range(1, int(num ** 0.5) + 1):
                    next_num = num - i * i
                    if next_num == 0:
                        return level
                    if next_num not in seen:
                        seen.add(next_num)
                        queue.append(next_num)


        
# @lc code=end

