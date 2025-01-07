#
# @lc app=leetcode id=622 lang=python
#
# [622] Design Circular Queue
#

# @lc code=start
class MyCircularQueue(object):

    def __init__(self, k):
        """
        :type k: int
        """
        self.array = [None] * k
        self.rear = self.front = 0
        

    def enQueue(self, value):
        """
        :type value: int
        :rtype: bool
        """
        if self.array[self.rear] is None:
            self.array[self.rear] = value
            self.rear = (self.rear + 1) % len(self.array)
            return True

        return False
        

    def deQueue(self):
        """
        :rtype: bool
        """
        if self.array[self.front] is not None:
            self.array[self.front] = None
            self.front = (self.front + 1) % len(self.array)
            return True

        return False
        

    def Front(self):
        """
        :rtype: int
        """
        return self.array[self.front] if self.array[self.front] is not None else -1
        

    def Rear(self):
        """
        :rtype: int
        """
        val = self.rear - 1
        if val < 0:
            val = len(self.array) - 1
        
        return self.array[val] if self.array[val] is not None else -1
        

    def isEmpty(self):
        """
        :rtype: bool
        """
        return self.array[self.front] is None and self.array[self.rear] is None
        

    def isFull(self):
        """
        :rtype: bool
        """
        return self.array[self.front] is not None and self.array[self.rear] is not None
        


# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()
# @lc code=end

