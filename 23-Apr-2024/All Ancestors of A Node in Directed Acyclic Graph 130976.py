# Problem: All Ancestors of A Node in Directed Acyclic Graph - https://leetcode.com/problems/all-ancestors-of-a-node-in-a-directed-acyclic-graph/

class Solution:
    def getAncestors(self, node_count: int, edges: List[List[int]]) -> List[List[int]]:
        graph = defaultdict(list)

        for u,v in edges:
            graph[u].append(v)

        ancestor = [[] for _ in range(node_count)]
       
        for node in range(node_count):
            queue = deque([node])
            visited = {node}
            while queue:
                now = queue.popleft()
                for nb in  graph[now]:
                    if nb not in visited:
                        visited.add(nb)
                        ancestor[nb].append(node)
                        queue.append(nb)
                
        return ancestor                   

