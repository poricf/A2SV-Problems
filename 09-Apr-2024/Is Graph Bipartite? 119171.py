# Problem: Is Graph Bipartite? - https://leetcode.com/problems/is-graph-bipartite/

class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        n = len(graph)
        colors = [-1] * n
        def check(start):
            q = deque()
            color = 0
            q.append((start,color))
            colors[start] = color


            while q:
                node,color = q.popleft()

                for child in graph[node]:
                    if colors[child] == -1:
                        colors[child] = (1 - color)
                        q.append((child,(1-color)))
                    else:
                        if colors[child] == color:
                            return False
            
            return True

        for i in range(len(colors)):
            if colors[i] == -1:
                flag = check(i)
                if not flag:
                    return False
        
        return True