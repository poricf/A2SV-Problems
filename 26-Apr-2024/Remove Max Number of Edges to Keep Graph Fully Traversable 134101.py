# Problem: Remove Max Number of Edges to Keep Graph Fully Traversable - https://leetcode.com/problems/remove-max-number-of-edges-to-keep-graph-fully-traversable/

class DSU:
    def __init__(self, n):
        self.rank = [0] * (n + 1)
        self.parent = list(range(n + 1))
        self.size = [1] * (n + 1)
        self.count = n

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
            return False
        if self.rank[rep_u] < self.rank[rep_v]:
            self.parent[rep_u] = rep_v
        elif self.rank[rep_v] < self.rank[rep_u]:
            self.parent[rep_v] = rep_u
        else:
            self.parent[rep_v] = rep_u
            self.rank[rep_u] += 1
        self.count -= 1

        return True

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
    def maxNumEdgesToRemove(self, n: int, edges: List[List[int]]) -> int:
        alice , bob = DSU(n),DSU(n)
        N = len(edges) # total edges
        visited = set()

        edges.sort(reverse = True)
        cnt = 0
        for edge in edges:
            typ , u , v = edge
            u -= 1
            v -= 1
            if typ == 3:
                if alice.Runion(u,v) | bob.Runion(u,v):
                    cnt += 1
            elif typ == 2:
                if bob.Runion(u,v):
                    cnt += 1
            else:
                if alice.Runion(u,v):
                    cnt += 1
        
        if alice.count != 1 or bob.count != 1: return -1
        return len(edges) - cnt