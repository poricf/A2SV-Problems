# Problem: D. Cutting a graph - https://codeforces.com/edu/course/2/lesson/7/1/practice/contest/289390/problem/D


import sys
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
                    
    def connected(self, x, y):
        return self.find(x) == self.find(y)




def solve():
    v,e,nop = ILT()
    uf = DSU(v)

    ops = []

    for _ in range(e):
        input()

    for _ in range(nop):
        ops.append(input().strip().split())

    ops.reverse()
    res = []
    for op in ops:
        if op[0] == "cut":
            uf.Runion(int(op[1]), int(op[2]))
        else:
            if uf.connected(int(op[1]), int(op[2])):
                res.append("YES")
            else:
                res.append("NO")

    res.reverse()
    for i in res:
        print(i)

T = 1

for _ in range(T):
    solve()