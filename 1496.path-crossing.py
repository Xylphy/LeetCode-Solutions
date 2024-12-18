#
# @lc app=leetcode id=1496 lang=python
#
# [1496] Path Crossing
#

# @lc code=start
class Solution(object):
    def isPathCrossing(self, path):
        """
        :type path: str
        :rtype: bool
        """
        seen = set()
        seen.add((0, 0))

        point = [0, 0]

        for p in path:
            if p == 'N':
                point[1] += 1
            elif p == 'S':
                point[1] -= 1
            elif p == 'E':
                point[0] += 1
            elif p == 'W':
                point[0] -= 1

            if (point[0] , point[1]) in seen:
                return True

            seen.add((point[0], point[1]))

        return False

        
# @lc code=end

