#
# @lc app=leetcode id=599 lang=python
#
# [599] Minimum Index Sum of Two Lists
#

# @lc code=start
class Solution(object):
    def findRestaurant(self, list1, list2):
        """
        :type list1: List[str]
        :type list2: List[str]
        :rtype: List[str]
        """
        map_list1 = {list1[i]: i for i in range(len(list1))}
        min_sum = float('inf')
        out = []

        for i in range(len(list2)):
            if list2[i] in map_list1:
                partial_sum = i + map_list1[list2[i]]
                if partial_sum < min_sum:
                    min_sum = partial_sum
                    out = [list2[i]]
                elif partial_sum == min_sum:
                    out.append(list2[i])

        return out
        
# @lc code=end

