#
# @lc app=leetcode id=1296 lang=python
#
# [1296] Divide Array in Sets of K Consecutive Numbers
#

# @lc code=start
class Solution(object):
    def isPossibleDivide(self, nums, k):
        import heapq
        from collections import Counter
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """

        if len(nums) % k != 0:
            return False

        counter = Counter(nums)
        heap = list(counter.keys())
        
        heapq.heapify(heap)

        while heap:
            first = heap[0]

            for num in range(first, first + k):
                if num not in counter:
                    return False

                counter[num] -= 1
                if counter[num] == 0:
                    if num != heap[0]:
                        return False

                    heapq.heappop(heap)

        return True
        
# @lc code=end

