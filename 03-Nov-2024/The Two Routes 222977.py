# Problem: The Two Routes - https://codeforces.com/problemset/problem/601/A


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



def get_path(end, parent, time):
    path = {}
    node = parent[end]
    time -= 1
    while time > 0:
        path[node] = time
        node = parent[node]
        time -= 1

    return path
def bfs(graph, start, end, will_crash = {}):
    queue = deque([start])
    visited = set([start])
    parent = {}
    count = 0

    while queue:
        for _ in range(len(queue)):
            node = queue.popleft()
            if node == end:
                return get_path(end, parent, count)
            
            if node in will_crash and will_crash[node] == count:
                continue
            
            for child in graph[node]:
                if child not in visited:
                    queue.append(child)
                    visited.add(child)
                    parent[child] = node
        count += 1

    return -1



def solve():
    n, m = ILT()
    railways = set()
    rail_graph = [[] for _ in range(n + 1)]
    for _ in range(m):
        u, v = ILT()
        rail_graph[u].append(v)
        rail_graph[v].append(u)
        railways.add((u, v))
        railways.add((v, u))
    
    rrp = [[] for _ in range(n + 1)]
    for i in range(1, n + 1):
        for j in range(i + 1, n + 1):
            if (i, j) in railways:
                continue

            rrp[i].append(j)
            rrp[j].append(i)

    start, end = 1, n
    
    rsp = bfs(rail_graph, start, end)
    rps = bfs(rrp, start, end)
    if rsp == -1 or rps == -1:
        print(-1)
    
    else:
        rsf = bfs(rrp, end, start, rsp)
        rfs = bfs(rail_graph, end, start, rps)

        if rsp == rfs:
            print(max(len(rfs), len(rps)) + 1)
        
        elif rps == rsf:
            print(max(len(rsf), len(rsp)) + 1)
        
        else:
            if rsp == rps:
                print(len(rsp) + 2)
            
            else:
                print(max(len(rsp), len(rps)) + 1)




for _ in range(I()):
    solve()