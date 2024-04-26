# Problem: Redundant Connection - https://leetcode.com/problems/redundant-connection/

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
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        n = len(edges)
        dsu = DSU(n)
        res = []
        for edge in edges:
            u , v = edge
            if dsu.find(u) != dsu.find(v):
                dsu.Runion(u,v)
            else:
                return [u,v]
        
       
