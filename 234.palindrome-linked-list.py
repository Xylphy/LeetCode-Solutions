#
# @lc app=leetcode id=234 lang=python
#
# [234] Palindrome Linked List
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: bool
        """
        slow = fast = head
        prev = None

        while fast and fast.next:
            fast = fast.next.next
            slow.next, prev, slow = prev, slow, slow.next

        fast = slow.next if fast else slow
        slow = prev

        while fast:
            if slow.val != fast.val:
                return False

            slow = slow.next
            fast = fast.next

        return True


        

# @lc code=end

