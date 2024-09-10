# Problem: E - Consecutive Subarrays - https://codeforces.com/gym/523525/problem/E


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
from itertools import *





def solve():
  n, m = ILT()

  a = ILT()
  a.reverse()

  p = list(accumulate(a))
  p = p[:len(p)-1]
  p.sort()
  p.reverse()

  x1 = sum(a)
  for i in range(m-1):
    x1 += p[i]

  print(x1)
  


  

solve()