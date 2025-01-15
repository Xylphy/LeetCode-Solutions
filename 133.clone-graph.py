#
# @lc app=leetcode id=133 lang=python
#
# [133] Clone Graph
#

# @lc code=start
# Definition for a Node.
""" class Node(object):
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else [] """

class Solution(object):
    def cloneGraph(self, node):
        """
        :type node: Node
        :rtype: Node
        """
        if not node:
            return None
        
        visited = {node: Node(node.val)}
        stack = [node]

        head = visited[node]

        while stack:
            current = stack.pop()
            for neighbor in current.neighbors:
                if neighbor not in visited:
                    visited[neighbor] = Node(neighbor.val)
                    stack.append(neighbor)
                visited[current].neighbors.append(visited[neighbor])

        return head
        

        
# @lc code=end

