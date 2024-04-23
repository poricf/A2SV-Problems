# Problem: Minimum Height Trees - https://leetcode.com/problems/minimum-height-trees/

class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        number_of_edges = [0 for _ in range(n)]
        graph = defaultdict(list)
        graphSet = set(range(0,(n)))
        # print(graphSet)
        for u , v in edges:
            graph[u].append(v)
            graph[v].append(u)
            number_of_edges[u] += 1
            number_of_edges[v] += 1
        
        q = deque()

        if len(graphSet) <= 2:
            return list(graphSet)
        for i in range(0,n):
            if number_of_edges[i] == 1:
                number_of_edges[i] -= 1
                graphSet.discard(i)
                q.append(i)
                

        
        while q:
            if len(graphSet) <= 2:
                return list(graphSet)

            for i in range(len(q)):
                node = q.popleft()
                for nb in graph[node]:
                    number_of_edges[nb] -= 1

                    if number_of_edges[nb] == 1:
                        q.append(nb)
                        graphSet.discard(nb)
            
            
                        


        