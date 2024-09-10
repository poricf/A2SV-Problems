# Problem: Fox And Names  (codeforces) - https://codeforces.com/contest/510/problem/C


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




def solve():
    n = int(input())
    indegree = defaultdict(int)
    graph = defaultdict(list)
    prev = ''
    for _ in range(n):
        s = input()
        if prev == '':
            prev = s
        else:
            p1 = 0
            while p1 < len(prev) and p1 < len(s):
                if s[p1] != prev[p1]:
                    graph[prev[p1]].append(s[p1])
                    indegree[s[p1]]+=1
                    break
                p1+=1
                if p1 == len(s) and p1 < len(prev):
                    return "Impossible"
            prev = s
    queue = deque([chr(i) for i in range(ord('a'), ord('z')+1) if indegree[chr(i)] == 0])
    ans = ''
    while queue:
        ele = queue.popleft()
        ans+=ele
        for negh in graph[ele]:
            indegree[negh]-=1
            if indegree[negh] == 0:
                queue.append(negh)
    
    return ans if len(ans) == 26 else "Impossible"
    
print(solve())