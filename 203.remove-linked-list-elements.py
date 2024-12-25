#
# @lc app=leetcode id=203 lang=python
#
# [203] Remove Linked List Elements
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode(object):
    # def __init__(self, val=0, next=None):
        # self.val = val
        # self.next = next


class Solution(object):
    def removeElements(self, head, val):
        """
        :type head: Optional[ListNode]
        :type val: int
        :rtype: Optional[ListNode]
        """
        current = dummy = ListNode(next=head)

        while current.next:
            if current.next.val == val:
                current.next = current.next.next
            else:
                current = current.next

        return dummy.next





# @lc code=end
