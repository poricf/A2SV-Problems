# Problem: Productive Meeting - https://codeforces.com/contest/1579/problem/D

######################################################################
###########     Author - Fahmi Dinsefa                  ##############
###########     Created at 4/17/2024                     ############## 
######################################################################

#############################################################################
import sys
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
#################################################################################################


def solve():

    n = I()
    a = ILT()
    original = [(a[i],i+1) for i in range(len(a))]
    max_heap = []
    
    for val,ind in original:
        if val != 0:
            heappush(max_heap,(-val,ind))
    

    talks = []
    
    while len(max_heap) > 1:
        p1 , i = heappop(max_heap)
        p2 , j = heappop(max_heap)
        talks.append((i,j))
            
        if (-p1) - 1:
            heappush(max_heap , (-(-p1 - 1),i))
        if (-p2) - 1:
            heappush(max_heap , (-(-p2 - 1),j))

    print(len(talks))
    for x,y in talks:
        print(x,y)


for _ in range(I()):
    solve()