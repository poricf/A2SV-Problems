# Problem: E - Yilal Doju - https://codeforces.com/gym/511242/problem/E

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
    n = I()
    a = ILT()
    a.append(1e8)

    def check(mid):
        n = len(a)
        mn = a[0]

        for i in range(1, n - 1):
            x = max(a[i], a[i - 1])
            y = min(a[i], a[i - 1])

            if (ceil(mn / 2) + ceil(a[i] / 2)) <= mid:
                return True

            if (ceil((a[i - 1] + a[i + 1]) / 2)) <= mid:
                return True

            if max(ceil(x / 2), ceil((x + y) / 3)) <= mid:
                return True

            mn = min(mn, a[i])
        return False
        
    l = 1 ; r = 10 ** 18
    
    best = -1

    while l <= r:
        m = (l+r) // 2

        if check(m):
            r = m - 1
            best = m
        else:
            l = m + 1
        
    print(best)

# for _ in range(I()):
solve()


    
