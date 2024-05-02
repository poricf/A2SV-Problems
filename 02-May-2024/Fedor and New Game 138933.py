# Problem: Fedor and New Game - https://codeforces.com/contest/467/problem/B

######################################################################
##########&#     Author - Fahmi Dinsefa                  ##############
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
from heapq import heapify, heappop, heapreplace, heappush




def solve():
    n , m , k = ILT()
    a = []
    for i in range(m):
        a.append(I())
    
    fedor = I()
    ans = 0
    for elm in a:
        x = elm^fedor
        if x.bit_count() <= k:
            ans += 1
    
    print(ans)

# for _ in range(I()):
solve()