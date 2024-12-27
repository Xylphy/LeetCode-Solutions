#
# @lc app=leetcode id=430 lang=python
#
# [430] Flatten a Multilevel Doubly Linked List
#

# @lc code=start
# Definition for a Node.
""" class Node(object):
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child """

class Solution(object):
    def flatten(self, head):
        """
        :type head: Node
        :rtype: Node
        """
        if not head:
            return None

        dummy = Node(0)
        dummy.next = head
        head.prev = dummy

        stack = [head]
        prev = dummy

        while stack:
            node = stack.pop()

            node.prev = prev
            prev.next = node

            if node.next:
                stack.append(node.next)

            if node.child:
                stack.append(node.child)
                node.child = None

            prev = node

        dummy.next.prev = None
        return dummy.next

        
# @lc code=end

