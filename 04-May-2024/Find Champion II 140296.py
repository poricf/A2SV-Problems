# Problem: Find Champion II - https://leetcode.com/problems/find-champion-ii/

class Solution:
    def findChampion(self, n: int, edges: List[List[int]]) -> int:
        indegrees = [0 for _ in range(n)]
        graph = defaultdict(list)
        answer = []
        q = deque()
        for ss , ff in edges:
            graph[ss].append(ff)
            indegrees[ff] += 1
        
        for ff,indegree in  enumerate(indegrees):
            if indegree == 0:
                q.append(ff)
        
        return q[0] if len(q) == 1 else -1
            

