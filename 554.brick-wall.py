#
# @lc app=leetcode id=554 lang=python
#
# [554] Brick Wall
#

# @lc code=start
class Solution(object):
    def leastBricks(self, wall):
        from collections import defaultdict
        """
        :type wall: List[List[int]]
        :rtype: int
        """
        hash_map = defaultdict(int)

        for row in wall:
            length = 0
            for brick in row[:-1]:
                length += brick
                hash_map[length] += 1

        return len(wall) - (max(hash_map.values()) if hash_map else 0)

        
# @lc code=end

