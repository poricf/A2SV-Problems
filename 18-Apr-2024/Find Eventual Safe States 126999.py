# Problem: Find Eventual Safe States - https://leetcode.com/problems/find-eventual-safe-states/

class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        colors = [0 for i in range(len(graph))]
        answer = []
        def dfs(node):
            if not graph[node]:
                answer.append(node)
                colors[node] = 2
                return True
            if colors[node] == 1:
                return False
            colors[node] = 1
            for child in graph[node]:
                if colors[child] == 2:
                    continue
                if not dfs(child):
                    return False
            
            answer.append(node)
            colors[node] = 2
            return True
            
        for i in range(len(graph)):
            if colors[i] == 0:
                dfs(i)
        
        return sorted(answer)