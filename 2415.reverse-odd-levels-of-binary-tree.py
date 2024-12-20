#
# @lc app=leetcode id=2415 lang=python
#
# [2415] Reverse Odd Levels of Binary Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def reverseOddLevels(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: Optional[TreeNode]
        """
        queue = [root]
        level = 0

        while queue:
            next_queue = []

            if level % 2 == 1:
                for i in range(len(queue) // 2):
                    queue[i].val, queue[-i - 1].val = queue[-i - 1].val, queue[i].val

            for node in queue:
                if node.left:
                    next_queue.append(node.left)
                if node.right:
                    next_queue.append(node.right)

            level += 1
            queue = next_queue

        return root
        
# @lc code=end

