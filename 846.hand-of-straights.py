#
# @lc app=leetcode id=846 lang=python
#
# [846] Hand of Straights
#

# @lc code=start
class Solution(object):
    def isNStraightHand(self, hand, groupSize):
        import heapq
        from collections import Counter
        """
        :type hand: List[int]
        :type groupSize: int
        :rtype: bool
        """

        if len(hand) % groupSize != 0:
            return False
        
        count = Counter(hand)
        heap = list(count.keys())

        heapq.heapify(heap)

        while heap:
            first = heap[0]

            for num in range(first, first + groupSize):
                if num not in count:
                    return False

                count[num] -= 1
                if count[num] == 0:
                    if num != heap[0]:
                        return False
                    heapq.heappop(heap)
                    

        return True
                
                        
        
# @lc code=end

