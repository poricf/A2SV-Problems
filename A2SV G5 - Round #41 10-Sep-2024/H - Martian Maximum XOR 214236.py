# Problem: H - Martian Maximum XOR - https://codeforces.com/gym/544854/problem/D

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
    n, k = ILT()
    a = ILT()
    t = sorted([[a[i], i] for i in range(n)])
    idx = []
    x = 10**10
    
    for i in range(n - 1):
        q = t[i][0] ^ t[i + 1][0]
        if q < x:
            idx = [t[i][1], t[i + 1][1]]
            x = q
    
    tw = (2 ** k) - 1 - max(a[idx[0]], a[idx[1]])
    print(idx[0] + 1, idx[1] + 1, tw)

for _ in range(I()):
    solve()