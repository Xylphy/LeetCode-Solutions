#
# @lc app=leetcode id=144 lang=python
#
# [144] Binary Tree Preorder Traversal
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def preorderTraversal(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[int]
        """
        list = []

        def preorder(root, list):
            if root:
                list.append(root.val)
                preorder(root.left, list)
                preorder(root.right, list)

        preorder(root, list)

        return list
        
# @lc code=end

