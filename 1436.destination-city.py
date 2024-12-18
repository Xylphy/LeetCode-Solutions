#
# @lc app=leetcode id=1436 lang=python
#
# [1436] Destination City
#

# @lc code=start
class Solution(object):
    def destCity(self, paths):
        """
        :type paths: List[List[str]]
        :rtype: str
        """
        paths_set = {path[0] for path in paths}
        for path in paths:
            if path[1] not in paths_set:
                return path[1]
        
# @lc code=end

