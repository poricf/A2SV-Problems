# Problem: D - Energy Crisis - https://codeforces.com/gym/511242/problem/D

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
    _,k = ILT()
    a = ILT()

    def check(x):
        ang, l = 0, 0
        for elm in a:
            if elm > x:
                d = elm-x
                ang += (d*((100-k)/100))
            if elm < x:
                l += x-elm
        return ang >= l
    
    l = min(a) ; r = max(a)
    
    best = -1

    for _ in range(50):
        m = (l+r) / 2

        if check(m):
            l = m
            best = m
        else:
            r = m 
        
    print(best)

# for _ in range(I()):
solve()


    


