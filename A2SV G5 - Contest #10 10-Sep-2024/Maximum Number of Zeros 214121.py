# Problem: Maximum Number of Zeros - https://codeforces.com/gym/514644/problem/D


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
    
    if a.count(a[0]) == n:
        return 0

    for x in a:
        if (x >= k and a[0] <= k) or (x <= k and a[0] >= k):
            return -1

    _gcd = abs(k - a[0])
    for i in a:
        _gcd = gcd(_gcd, abs(k - i))
    
    ans = 0
    for i in a:
        ans += (abs(k - i) // _gcd - 1)
    
    return ans


t = I()
for _ in range(t):
    print(solve())