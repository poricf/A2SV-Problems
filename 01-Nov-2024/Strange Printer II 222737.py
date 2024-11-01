# Problem: Strange Printer II - https://leetcode.com/problems/strange-printer-ii/

from collections import defaultdict
from typing import List

INF = float("inf")
NINF = float("-inf")

class Solution:
    def hasCycle(self, graph):
        indegree = defaultdict(int)
        for node in graph:
            for neighbor in graph[node]:
                indegree[neighbor] += 1

        queue = deque()
        for node in graph:
            if indegree[node] == 0:
                queue.append(node)

        while queue:
            node = queue.popleft()

            for neighbor in graph[node]:
                indegree[neighbor] -= 1
                if indegree[neighbor] == 0:
                    queue.append(neighbor)

        for node in graph:
            if indegree[node] > 0:
                return True

        return False

    def isPrintable(self, tg: List[List[int]]) -> bool:

        n = len(tg)
        m = len(tg[0])
        colors = defaultdict(lambda: [INF, INF, NINF, NINF])
        graph = defaultdict(set)

        for i in range(n):
            for j in range(m):
                now = tg[i][j]
                colors[now][0] = min(colors[now][0], i)

                
                colors[now][1] = min(colors[now][1], j)
                colors[now][2] = max(colors[now][2], i)
                colors[now][3] = max(colors[now][3], j)
        
        for color, value in colors.items():
            istart, jstart, iend, jend = value

            for i in range(istart, iend + 1):
                for j in range(jstart, jend + 1):
                    if tg[i][j] != color:
                        graph[color].add(tg[i][j])
        
        if self.hasCycle(graph):
            return False
        
        return True