# Problem: Employee Importance - https://leetcode.com/problems/employee-importance/

"""
# Definition for Employee.
class Employee:
    def __init__(self, id: int, importance: int, subordinates: List[int]):
        self.id = id
        self.importance = importance
        self.subordinates = subordinates
"""

class Solution:
    def getImportance(self, employees: List['Employee'], id: int) -> int:
        graph = defaultdict(list)
        graph_sub = defaultdict(list)
        for emp in employees:
            graph[emp.id] = emp.importance
            graph_sub[emp.id] = emp.subordinates

        print(graph , graph_sub)
        q = deque([id])
        total = 0
        while q:
            node = q.popleft()
            total += graph[node]
            for i in graph_sub[node]:
                q.append(i)
        return total


        
