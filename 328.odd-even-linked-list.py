#
# @lc app=leetcode id=328 lang=python
#
# [328] Odd Even Linked List
#


# @lc code=start
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def oddEvenList(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        if not head:
            return None

        curr_odd, curr_even = odd, even = head, head.next

        while curr_even and curr_even.next:
            curr_odd.next = curr_odd.next.next
            curr_even.next = curr_even.next.next
            curr_odd, curr_even = curr_odd.next, curr_even.next

        curr_odd.next = even
        return odd
        


# @lc code=end
