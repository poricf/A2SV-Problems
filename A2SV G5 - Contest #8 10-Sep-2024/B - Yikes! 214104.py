# Problem: B - Yikes! - https://codeforces.com/gym/511242/problem/B


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
  a = ILT()
  m = I()
  spi = ILT()

  order = [(1, a[0])]


  for i in range(1, n):
    order.append((order[-1][1]+1, order[-1][1]+ a[i]))

  for i in range(m):
    idx = bisect_left(order, (spi[i], float('inf')))
    print(idx)


       



solve()