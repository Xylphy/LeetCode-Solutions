#
# @lc app=leetcode id=2073 lang=python
#
# [2073] Time Needed to Buy Tickets
#

# @lc code=start
class Solution(object):
    def timeRequiredToBuy(self, tickets, k):
        """
        :type tickets: List[int]
        :type k: int
        :rtype: int
        """
        seconds = 0

        for i in range(len(tickets)):
            if i <= k:
                seconds += min(tickets[i], tickets[k])
            else:
                seconds += min(tickets[i], tickets[k] - 1)

        return seconds

        
# @lc code=end

