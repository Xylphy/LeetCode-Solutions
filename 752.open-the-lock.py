#
# @lc app=leetcode id=752 lang=python
#
# [752] Open the Lock
#

# @lc code=start
class Solution(object):
    def openLock(self, deadends, target):
        import collections
        """
        :type deadends: List[str]
        :type target: str
        :rtype: int
        """
        deadends = set(deadends)

        def bfs(start):
            queue = collections.deque([(start, 0)])
            visited = set([start])

            while queue:
                node, depth = queue.popleft()
                if node == target:
                    return depth
                if node in deadends:
                    continue
                for i in range(4):
                    for d in [-1, 1]:
                        new_node = node[:i] + str((int(node[i]) + d) % 10) + node[i+1:]
                        if new_node not in visited:
                            visited.add(new_node)
                            queue.append((new_node, depth + 1))
            return -1

        return bfs("0000")
        

        
# @lc code=end

