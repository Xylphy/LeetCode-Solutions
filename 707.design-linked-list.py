#
# @lc app=leetcode id=707 lang=python
#
# [707] Design Linked List
#


# @lc code=start
class Node:
    def __init__(self, val):
        self.val = val
        self.prev = self.next = None

    def __init__(self, val, next, prev):
        self.val = val
        self.next = next
        self.prev = prev


class MyLinkedList(object):

    def __init__(self):
        self.head = self.tail = None
        self.size = 0

    def addBetween(self, prev, next, val):
        self.size += 1
        node = Node(val, next, prev)
        if prev:
            prev.next= node
        if next:
            next.prev = node
        return node

    def removeBetween(self, prev, next):
        if prev:
            prev.next = next
        if next:
            next.prev = prev

        self.size -= 1

    def get(self, index):
        """
        :type index: int
        :rtype: int
        """
        if index < 0 or index >= self.size:
            return -1

        if index < self.size // 2:
            current = self.head
            for _ in range(index):
                current = current.next
        else:
            current = self.tail
            for _ in range(self.size - index - 1):
                current = current.prev

        return current.val

    def addAtHead(self, val):
        """
        :type val: int
        :rtype: None
        """
        if not self.head:
            self.head = self.tail = self.addBetween(None, None, val)
        else:
            self.head = self.addBetween(None, self.head, val)

    def addAtTail(self, val):
        """
        :type val: int
        :rtype: None
        """
        if not self.tail:
            self.head = self.tail = self.addBetween(None, None, val)
        else:
            self.tail = self.addBetween(self.tail, None, val)

    def addAtIndex(self, index, val):
        """
        :type index: int
        :type val: int
        :rtype: None
        """
        if index == self.size:
            self.addAtTail(val)
        elif index <= 0:
            self.addAtHead(val)
        else:
            current = self.head

            if not current:
                return

            for _ in range(index - 1):
                current = current.next

            if not current:
                return

            current.next = self.addBetween(current, current.next, val)

    def deleteAtIndex(self, index):
        """
        :type index: int
        :rtype: None
        """
        if index < 0 or index >= self.size:
            return

        if index < self.size // 2:
            current = self.head
            for _ in range(index):
                current = current.next
        else:
            current = self.tail
            for _ in range(self.size - index - 1):
                current = current.prev

        self.removeBetween(current.prev, current.next)

        if index == 0:
            self.head = self.head.next
        if index == self.size:
            self.tail = self.tail.prev


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)
# @lc code=end
