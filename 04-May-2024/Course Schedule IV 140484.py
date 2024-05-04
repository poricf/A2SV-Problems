# Problem: Course Schedule IV - https://leetcode.com/problems/course-schedule-iv/description/

class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        n = numCourses
        if not prerequisites:
            return [False]*len(queries)
        indegree = [0 for _ in range(n)]
        graph = [[] for _ in range(n)]



        for node1, node2 in prerequisites:
            graph[node1].append(node2)
            indegree[node2] += 1
        

        answer = [set() for _ in range(n)]

        def bfs():
            queue = deque([i for i in range(n) if indegree[i] == 0])

            while queue:
                node = queue.popleft()

                for neighbour in graph[node]:
                    indegree[neighbour] -= 1
                    answer[neighbour] |= answer[node]
                    answer[neighbour].add(node)

                    if indegree[neighbour] == 0:
                        queue.append(neighbour)
        
        bfs()
        result = []
        for a,b in queries:
            if a in answer[b]:
                result.append(True)
            else:
                result.append(False)
        return result 



