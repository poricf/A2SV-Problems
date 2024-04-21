# Problem: Course Schedule II - https://leetcode.com/problems/course-schedule-ii/description/

class Solution:
    def findOrder(self, n: int, prerequisites: List[List[int]]) -> List[int]:
        indegrees = [0 for _ in range(n)]
        graph = defaultdict(list)
        answer = []
        q = deque()
        for course , pre in prerequisites:
            graph[pre].append(course)
            indegrees[course] += 1
        
        for course,indegree in  enumerate(indegrees):
            if indegree == 0:
                q.append(course)
        
        while q:
            course = q.popleft()
            answer.append(course)

            for child in graph[course]:
                indegrees[child] -= 1
                if indegrees[child] == 0:
                    q.append(child)
            
        
        if len(answer) != n:
            return []
        return answer
            

