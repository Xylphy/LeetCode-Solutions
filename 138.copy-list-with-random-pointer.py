#
# @lc app=leetcode id=138 lang=python
#
# [138] Copy List with Random Pointer
#

# @lc code=start
# Definition for a Node.
""" class Node:
    def __init__(self, x, next=None, random=None):
        self.val = int(x)
        self.next = next
        self.random = random """

class Solution(object):
    def copyRandomList(self, head):
        """
        :type head: Node
        :rtype: Node
        """
        if not head: return None

        curr = head
        nodes = {}

        while curr:
            nodes[curr] = Node(curr.val)
            curr = curr.next

        curr = head
        while curr:
            nodes[curr].next = nodes.get(curr.next)
            nodes[curr].random = nodes.get(curr.random)
            curr = curr.next

        return nodes[head]


        
# @lc code=end

