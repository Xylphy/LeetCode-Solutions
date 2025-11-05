#
# @lc app=leetcode id=2807 lang=python
#
# [2807] Insert Greatest Common Divisors in Linked List
#


# @lc code=start
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def insertGreatestCommonDivisors(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """

        def gcd(a, b):
            while b:
                a, b = b, a % b
            return a

        current = head
        while current and current.next:
            next_node = current.next
            gcd_value = gcd(current.val, next_node.val)
            new_node = ListNode(gcd_value)
            current.next = new_node
            new_node.next = next_node
            current = next_node

        return head


# @lc code=end
