# Problem: E - Machine Testing - https://codeforces.com/gym/513152/problem/E


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
    h = ILT()
    pr = ILT()

    ans = 0
    stack = [(INF, pr[0])]
    for i in range(1, n):
        curr = 0
        while h[i] > (stack[-1][0]-curr)*stack[-1][-1]:
            t, p = stack.pop()
            h[i] -= (t-curr)*p
            curr += t-curr
        curr += ceil(h[i]/stack[-1][-1])
        stack.append((curr, pr[i]))
        ans = max(ans, curr)
    print(ans)

t = int(input())
for _ in range(t):
    solve()
