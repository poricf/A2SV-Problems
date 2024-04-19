# Problem: Longest Cycle in a Graph - https://leetcode.com/problems/longest-cycle-in-a-graph/

class Solution:
    def longestCycle(self, edges: List[int]) -> int:
        n = len(edges)
        max_nodes , nodes = -1,0
        visited = set()
        colors = [0 for i in range(n)]

        def count_nodes(node):
            nonlocal max_nodes , nodes
            if node in visited:
                return
            
            visited.add(node)
            nodes += 1

            count_nodes(edges[node])

            max_nodes = max(nodes,max_nodes)

            return

        def topsort(node):
            nonlocal nodes
            if colors[node] == 1:
                nodes = 0
                count_nodes(node)
                return
            colors[node] = 1

            if edges[node] == -1:
                colors[node] = 2
                return

            if colors[edges[node]] == 2:
                colors[node] = 2
                return

            topsort(edges[node])
            colors[node] = 2

        for i in range(n):
            if colors[i] == 0 and edges[i] != -1:
                topsort(i)
        
        return max_nodes