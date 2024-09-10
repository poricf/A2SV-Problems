# Problem: C - Spaceship Attack - https://codeforces.com/gym/511242/problem/C


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
    pass

def solve():
  s, b = ILT()
  a = ILT()
  bs = []
  c = [0]

  for _ in range(b):
    bs.append(ILT())

  bs.sort()
  for base, gold in bs:
    c.append(c[-1]+gold)


  for num in a:
    idx = bisect_left(bs, [num, float('inf')])
    print(c[idx], end=' ')
 

solve()