#
# @lc app=leetcode id=652 lang=python
#
# [652] Find Duplicate Subtrees
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def findDuplicateSubtrees(self, root):
        from collections import defaultdict
        """
        :type root: Optional[TreeNode]
        :rtype: List[Optional[TreeNode]]
        """
        seen = defaultdict(int)
        duplicates = []

        def traverse(node):
            if not node:
                return None

            left = traverse(node.left)
            right = traverse(node.right)
            subtree = (node.val, left, right)

            if seen[subtree] == 1:
                duplicates.append(node)
            seen[subtree] += 1

            return subtree
        
        traverse(root)

        return list(duplicates)


        
# @lc code=end
