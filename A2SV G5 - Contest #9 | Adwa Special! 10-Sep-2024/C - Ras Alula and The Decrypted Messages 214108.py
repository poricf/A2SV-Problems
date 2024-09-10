# Problem: C - Ras Alula and The Decrypted Messages - https://codeforces.com/gym/513152/problem/C


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
  n, m = ILT()
  s = S()
  t = S()

  prefix = [0]

  for i in range(n):
    prefix.append(prefix[-1] + (ord(s[i])- ord('a')+1))


  l = 0
  r = m
  sum_ = 0
  for i in range(m):
    sum_ += (ord(t[i]) - ord('a') + 1)


  while r < n+1:
    if prefix[r] - prefix[l] == sum_:
      print('YES')
      return
    
    l+=1
    r+=1
    
  print('NO')




for _ in range(I()):
  solve()