# Problem: I - MST for Promptness - https://codeforces.com/gym/544854/problem/E

import sys
from collections import defaultdict

sys.setrecursionlimit(10**3)
INF = float('inf')
N = 10**5 + 10
alpha = '/abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ/'

def I(): return int(sys.stdin.readline().strip())
def ILT(): return list(map(int, sys.stdin.readline().strip().split()))
def S(): return sys.stdin.readline().strip()
def SLT(): return sys.stdin.readline().strip().split()
def DIG(): return [int(i) for i in (list(sys.stdin.readline().strip()))]
def CHAR(): return list(sys.stdin.readline().strip())
ORD = lambda: [ord(char) for char in sys.stdin.readline().strip()]

from collections import Counter, defaultdict, deque
from bisect import bisect_right, bisect_left
from math import ceil, sqrt, gcd
from heapq import heapify, heappop, heapreplace, heappush

class DSU:
    def __init__(self, n):
        self.rank = [0] * (n + 1)
        self.parent = list(range(n + 1))
        self.size = [1] * (n + 1)
        self.count = n

    def find(self, node):
        if node != self.parent[node]:
            self.parent[node] = self.find(self.parent[node])
        return self.parent[node]

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

    def cnt(self):
        return self.count

def solve():
    n, m = ILT()  # Read number of nodes and edges
    degree = [0] * (n + 1)
    graph = defaultdict(set)

    for _ in range(m):
        a, b = ILT()  
        degree[a] += 1
        degree[b] += 1
        graph[a].add(b)
        graph[b].add(a)

    g = [(degree[node], node) for node in range(1, n + 1)]
    g.sort()

    dsu = DSU(n)
    start = g[0][1]

    for d, node in g:
        if node != start and dsu.find(start) == dsu.find(node):
            continue

        for child in range(1, n + 1):
            if child not in graph[node] and child != node:
                dsu.Runion(child, node)

        if dsu.size[dsu.find(node)] == n:
            print(0)
            return

    print(dsu.cnt() - 1)

T = 1
for _ in range(T):
    solve()