# Problem: Parallel Courses III - https://leetcode.com/problems/parallel-courses-iii/

class Solution:
    def minimumTime(self, n: int, relations: List[List[int]], time: List[int]) -> int:

        indegree = [0 for _ in range(n+1)]
        graph = [[] for _ in range(n+1)]

        for node1, node2 in relations:
            graph[node1].append(node2)
            indegree[node2] += 1
        

        total_time = [0] + time

        def bfs():
            queue = deque([i for i in range(n+1) if indegree[i] == 0])

            while queue:
                node = queue.popleft()

                for nb in graph[node]:
                    indegree[nb] -= 1
                    total_time[nb] = max(total_time[nb], total_time[node] + time[nb-1])

                    if indegree[nb] == 0:
                        queue.append(nb)
        
        bfs()

        return max(total_time)



