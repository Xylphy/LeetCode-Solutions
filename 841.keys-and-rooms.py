#
# @lc app=leetcode id=841 lang=python
#
# [841] Keys and Rooms
#

# @lc code=start
class Solution(object):
    def canVisitAllRooms(self, rooms):
        """
        :type rooms: List[List[int]]
        :rtype: bool
        """
        stack = [0]
        seen = set([0])
        visited = 1

        while stack:
            room = stack.pop()
            for key in rooms[room]:
                if key not in seen:
                    seen.add(key)
                    visited += 1
                    stack.append(key)

        return visited == len(rooms)

        
# @lc code=end

