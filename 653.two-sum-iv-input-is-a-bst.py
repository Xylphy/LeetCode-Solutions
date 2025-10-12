#
# @lc app=leetcode id=653 lang=python
#
# [653] Two Sum IV - Input is a BST
#


# @lc code=start
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def findTarget(self, root, k):
        """
        :type root: Optional[TreeNode]
        :type k: int
        :rtype: bool
        """
        if not root:
            return False

        class BSTIterator:
            def __init__(self, node, forward=True):
                self.stack = []
                self.forward = forward
                self._push(node)

            def _push(self, node):
                while node:
                    self.stack.append(node)
                    node = node.left if self.forward else node.right

            def hasNext(self):
                return bool(self.stack)

            def peek(self):
                return self.stack[-1].val

            def next(self):
                node = self.stack.pop()
                val = node.val
                if self.forward:
                    self._push(node.right)
                else:
                    self._push(node.left)
                return val

        left_it = BSTIterator(root, True)
        right_it = BSTIterator(root, False)

        while (
            left_it.hasNext()
            and right_it.hasNext()
            and left_it.peek() < right_it.peek()
        ):
            s = left_it.peek() + right_it.peek()
            if s == k:
                return True
            if s < k:
                left_it.next()
            else:
                right_it.next()

        return False


# @lc code=end
