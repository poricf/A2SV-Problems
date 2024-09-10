# Problem: Disjoint Sets Union 2 - https://codeforces.com/edu/course/2/lesson/7/1/practice/contest/289390/problem/B


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
    def __init__(self, size):
        self.parent = {i:i for i in range(1, 1+size)} 
        self.size = {i:1 for i in range(1, 1+size)}
        self.min = {i:i for i in range(1, 1+size)}
        self.max = {i:i for i in range(1, 1+size)}
        
    def find(self, x):
        if self.parent[x] == x:
            return x
        parent = self.find(self.parent[x])
        self.parent[x] = parent
        return parent
    def get(self, x):
        parent = self.find(x)
        return [self.min[parent], self.max[parent], self.size[parent]]
    
    def union(self, x, y):
        rooty = self.find(y)
        rootx = self.find(x)
        if rootx == rooty:
            return
        if self.size[rootx] > self.size[rooty]:
            self.parent[rooty] = rootx
            self.size[rootx] += self.size[rooty]
            self.min[rootx] = min(self.min[rootx], self.min[rooty])
            self.max[rootx] = max(self.max[rootx], self.max[rooty])
        else:
            self.parent[rootx] = rooty
            self.size[rooty] += self.size[rootx]
            self.min[rooty] = min(self.min[rooty], self.min[rootx])
            self.max[rooty] = max(self.max[rooty], self.max[rootx])
            
n, q = ILT()
uf = DSU(n)
for _ in range(q):
    cmd = input().strip().split()
    if cmd[0] == "union":
        uf.union(int(cmd[1]), int(cmd[2]))
    else:
        print(*uf.get(int(cmd[1])))