# Problem: Cyclic Components - https://codeforces.com/problemset/problem/977/E

######################################################################
###########     Author - Fahmi Dinsefa                  ##############
###########     Created at 4/8/2024                     ############## 
######################################################################

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




def solve():
    n , m = ILT()
    graph = defaultdict(list)
    for i in range(m):
        u,v = ILT()
        graph[u].append(v)
        graph[v].append(u)
    cnt = 0
    visited = set()
    def dfs(node):
        stack = [node]
        ans = True

        while stack:
            node = stack.pop()
            if node not in visited:
                visited.add(node)
                if len(graph[node]) != 2:
                    ans = False
            
                for child in graph[node]:
                    if child not in visited:
                        stack.append(child)

        return ans
    for i in range(1,n+1):
        if i not in visited:
            if dfs(i):
                cnt += 1
    print(cnt)

# for _ in range(I()):
solve()