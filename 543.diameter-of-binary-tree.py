#
# @lc app=leetcode id=543 lang=python
#
# [543] Diameter of Binary Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def height(self, root, diameter):
        if root is None:
            return 0

        left = self.height(root.left, diameter)
        right = self.height(root.right, diameter)
        diameter[0] = max(diameter[0], left + right)
        return max(left, right) + 1

    def diameterOfBinaryTree(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        diameter = [0]
        self.height(root, diameter)
        return diameter[0]
        
# @lc code=end

