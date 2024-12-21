#
# @lc app=leetcode id=2872 lang=python
#
# [2872] Maximum Number of K-Divisible Components
#

# @lc code=start
class Solution(object):
    def maxKDivisibleComponents(self, n, edges, values, k):
        """
        :type n: int
        :type edges: List[List[int]]
        :type values: List[int]
        :type k: int
        :rtype: int
        """
        graph = [[] for _ in range(n)]
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)

        result = [0]

        def dfs(node, parent, result, k, values, graph):
            sum = 0
            for child in graph[node]:
                if child == parent:
                    continue

                sum += dfs(child, node, result, k, values, graph)
                sum %= k

            sum += values[node]
            sum %= k
            
            if sum == 0:
                result[0] += 1

            return sum

        dfs(0, -1, result, k, values, graph)

        return result[0]


        
        
# @lc code=end

