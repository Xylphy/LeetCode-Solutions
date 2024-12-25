#
# @lc app=leetcode id=515 lang=python
#
# [515] Find Largest Value in Each Tree Row
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution(object):
    def largestValues(self, root):
        from collections import deque
        """
        :type root: Optional[TreeNode]
        :rtype: List[int]
        """
        if not root:
            return []

        queue = deque([root])
        result = []

        while queue:
            max_val = float('-inf')
            for _ in range(len(queue)):
                node = queue.popleft()
                max_val = max(max_val, node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            
            result.append(max_val)

        return result

        
# @lc code=end

