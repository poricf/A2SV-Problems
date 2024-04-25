# Problem: Min Cost to Connect All Points - https://leetcode.com/problems/min-cost-to-connect-all-points/

class DSU:
    def __init__(self, n):
        self.rank = [0] * (n + 1)
        self.parent = list(range(n + 1))
        self.size = [1] * (n + 1)

    def find(self, node):
        if node == self.parent[node]:
            return node

        stack = []
        while node != self.parent[node]:
            stack.append(node)
            node = self.parent[node]

        # Path compression
        for n in stack:
            self.parent[n] = node

        return node

    def Runion(self, u, v):
        rep_u = self.find(u)
        rep_v = self.find(v)
        if rep_u == rep_v:
            return
        if self.rank[rep_u] < self.rank[rep_v]:
            self.parent[rep_u] = rep_v
        elif self.rank[rep_v] < self.rank[rep_u]:
            self.parent[rep_v] = rep_u
        else:
            self.parent[rep_v] = rep_u
            self.rank[rep_u] += 1

    def Sunion(self, u, v):
        rep_u = self.find(u)
        rep_v = self.find(v)
        if rep_u == rep_v:
            return
        if self.size[rep_u] < self.size[rep_v]:
            self.parent[rep_u] = rep_v
            self.size[rep_v] += self.size[rep_u]
        else:
            self.parent[rep_v] = rep_u
            self.size[rep_u] += self.size[rep_v]

class Solution:
    def ToEdgeList(self,points):
        n = len(points)
        edges = []
        for i in range(n):
            x1 , y1 = points[i]
            for j in range(i+1,n):
                x2 , y2 = points[j]

                dist = abs(x1 - x2) + abs(y1 - y2)
                edges.append((dist,i,j))
        return edges
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        n = len(points)
        edges = self.ToEdgeList(points)
        edges.sort()
        dsu = DSU(n)
        ans = 0
        for edge in edges:
            wt , u , v = edge
            if dsu.find(u) != dsu.find(v):
                ans += wt
                dsu.Runion(u,v)

        return ans