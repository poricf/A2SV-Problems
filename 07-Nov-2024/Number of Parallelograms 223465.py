# Problem: Number of Parallelograms - https://codeforces.com/contest/660/problem/D

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
    n = I()
    x, y = [], []
    for _ in range(n):
        xi, yi = ILT()
        x.append(xi)
        y.append(yi)
    
    cnt = defaultdict(int)
    for i in range(n):
        for j in range(i):
            cx = x[i] + x[j]
            cy = y[i] + y[j]
            cnt[(cx, cy)] += 1

    ans = 0
    for value in cnt.values():
        ans += value * (value - 1) // 2

    print(ans)

# for _ in range(I()):
solve()
