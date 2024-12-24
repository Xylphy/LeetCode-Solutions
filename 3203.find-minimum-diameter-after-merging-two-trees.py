#
# @lc app=leetcode id=3203 lang=python
#
# [3203] Find Minimum Diameter After Merging Two Trees
#

# @lc code=start
class Solution(object):
    def minimumDiameterAfterMerge(self, edges1, edges2):
        """
        :type edges1: List[List[int]]
        :type edges2: List[List[int]]
        :rtype: int
        """
        graph_tree1 = [[] for _ in range(len(edges1) + 1)]
        graph_tree2 = [[] for _ in range(len(edges2) + 1)]

        for edge in edges1:
            graph_tree1[edge[0]].append(edge[1])
            graph_tree1[edge[1]].append(edge[0])

        for edge in edges2:
            graph_tree2[edge[0]].append(edge[1])
            graph_tree2[edge[1]].append(edge[0])

        def bfs(i, graph):
            level = 0

            seen = set(graph[i])
            seen.add(i)

            start = graph[i]

            while start:
                next_level = []

                for node in start:
                    for next_node in graph[node]:
                        if next_node not in seen:
                            next_level.append(next_node)
                            seen.add(next_node)

                start = next_level

                level += 1
            
            return level

        return min([bfs(i, graph_tree1) for i in range(len(graph_tree1))]) + min([bfs(i, graph_tree2) for i in range(len(graph_tree2))]) + 1

        
# @lc code=end

