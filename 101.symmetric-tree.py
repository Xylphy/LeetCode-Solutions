#
# @lc app=leetcode id=101 lang=python
#
# [101] Symmetric Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: bool
        """
        if not root:
            return True

        queue = [root.left, root.right]

        while queue:
            n = len(queue)
            next_queue = []
            for i in range(n // 2):
                if not queue[i] and not queue[n - i - 1]:
                    continue

                if not queue[i] or not queue[n - i - 1]:
                    return False

                if queue[i].val != queue[n - i - 1].val:
                    return False

            for _ in range(n):
                node = queue.pop(0)
                if node:
                    next_queue.append(node.left)
                    next_queue.append(node.right)

            queue = next_queue

        return True
        
        
        
# @lc code=end

