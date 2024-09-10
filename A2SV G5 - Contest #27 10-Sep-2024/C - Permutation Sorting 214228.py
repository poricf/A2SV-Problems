# Problem: C - Permutation Sorting - https://codeforces.com/gym/538762/problem/C

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
    res = 0
    n = I()
    arr = ILT()
    pos = [0] * n
    
    for i in range(len(arr)):
        pos[arr[i] - 1] = i
    
    for j in range(1, len(pos)):
        if pos[j - 1] > pos[j]:
            res += 1
            
    print(res)

for _ in range(I()):
    solve()