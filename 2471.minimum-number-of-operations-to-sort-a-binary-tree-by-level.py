#
# @lc app=leetcode id=2471 lang=python
#
# [2471] Minimum Number of Operations to Sort a Binary Tree by Level
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution(object):
    def minimumOperations(self, root):
        from collections import deque
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        def _get_min_swaps(original):
            swaps = 0
            target = sorted(original)

            pos = {val: idx for idx, val in enumerate(original)}

            for i in range(len(original)):
                if original[i] != target[i]:
                    swaps += 1

                    cur_pos = pos[target[i]]
                    pos[original[i]] = cur_pos
                    original[cur_pos] = original[i]

            return swaps

        queue = deque([root])
        total_swaps = 0

        while queue:
            level_size = len(queue)
            level_values = []

            for _ in range(level_size):
                node = queue.popleft()
                level_values.append(node.val)

                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

            total_swaps += _get_min_swaps(level_values)

        return total_swaps

        
# @lc code=end

