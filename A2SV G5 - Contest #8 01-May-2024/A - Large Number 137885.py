# Problem: A - Large Number - https://codeforces.com/gym/511242/problem/A

######################################################################
###########     Author - Fahmi Dinsefa                  ##############
###########     Created at 5/1/2024                     ############## 
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
    n,k = ILT()
    a = CHAR()
    ind = n
    for i in range(n):
        if a[i] < str(k):
            ind = i
            break
    
    a.insert(ind,str(k))

    print("".join(a))

    

for _ in range(I()):
    solve()