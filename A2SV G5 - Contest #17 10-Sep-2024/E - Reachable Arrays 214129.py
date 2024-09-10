# Problem: E - Reachable Arrays - https://codeforces.com/gym/524965/problem/E


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


MOD = 998244353


def solve():
    n = I()
    a = ILT()
    
    mn_nx = [0] * n
    sm = [0] * (n + 2)
    nx = [0] * n

    mn = []
    mn_nx[n - 1] = n
    sm[n] = 1

    for pos in range(n - 1, -1, -1):
        while mn and a[mn[-1]] > a[pos]:
            mn.pop()
        mn_nx[pos] = n if not mn else mn[-1]
        mn.append(pos)

        nxt_pos = mn_nx[pos]
        dp_pos = (sm[pos + 1] - sm[nxt_pos + 1]) % MOD
        if nxt_pos != n:
            dp_pos = (dp_pos + nx[nxt_pos]) % MOD
            nx[pos] = (sm[nxt_pos] - sm[nxt_pos + 1] + nx[nxt_pos]) % MOD
        
        sm[pos] = (dp_pos + sm[pos + 1]) % MOD

    res = 0
    mn = a[0]
    for i in range(n):
        mn = min(mn, a[i])
        if a[i] == mn:
            res = (res + sm[i] - sm[i + 1]) % MOD

    print(res)


for _ in range(I()):
    solve()

