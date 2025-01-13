#
# @lc app=leetcode id=155 lang=python
#
# [155] Min Stack
#

# @lc code=start
import heapq

class MinStack(object):

    def __init__(self):
        self.heap = []
        self.stack = []
        

    def push(self, val):
        """
        :type val: int
        :rtype: None
        """
        heapq.heappush(self.heap, val)
        self.stack.append(val)
        

    def pop(self):
        """
        :rtype: None
        """
        if not self.stack:
            return

        self.heap.remove(self.stack.pop())
        heapq.heapify(self.heap)
        

    def top(self):
        """
        :rtype: int
        """
        return self.stack[-1]
        

    def getMin(self):
        """
        :rtype: int
        """
        return self.heap[0]
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
# @lc code=end

