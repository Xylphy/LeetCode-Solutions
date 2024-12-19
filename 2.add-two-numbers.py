#
# @lc app=leetcode id=2 lang=python
#
# [2] Add Two Numbers
#

# @lc code=start
# Definition for singly-linked list.
""" class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next """
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: Optional[ListNode]
        :type l2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        carry = 0
        head = dummy = ListNode()

        while l1 or l2 or carry == 1:
            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0

            carry, val = divmod(val1 + val2 + carry, 10)
            dummy.next = ListNode(val)
            dummy = dummy.next

            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None

        return head.next
        

        
# @lc code=end

