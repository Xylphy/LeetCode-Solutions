#
# @lc app=leetcode id=225 lang=python
#
# [225] Implement Stack using Queues
#

# @lc code=start
from collections import deque

class MyStack(object):

    def __init__(self):
        self.in_queue = deque()
        self.out_queue = deque()
        

    def push(self, x):
        """
        :type x: int
        :rtype: None
        """
        self.in_queue.append(x)
        

    def pop(self):
        """
        :rtype: int
        """
        self.top()
        return self.out_queue.pop()
        

    def top(self):
        """
        :rtype: int
        """
        while self.in_queue:
            self.out_queue.append(self.in_queue.popleft())

        return self.out_queue[-1]

        

    def empty(self):
        """
        :rtype: bool
        """
        return not self.in_queue and not self.out_queue
        


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()
# @lc code=end

