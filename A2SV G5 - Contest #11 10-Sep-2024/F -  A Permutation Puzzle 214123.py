# Problem: F -  A Permutation Puzzle - https://codeforces.com/gym/515998/problem/F


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
    s = S()
    a = ILT()

    lcm = 1
    vis = [0] * n
    for i in range(n):
        if vis[i]:
            continue
        cur = []
        ind = i
        while not vis[ind]:
            cur.append(s[ind])
            vis[ind] = 1
            ind = a[ind] - 1
        ns = "".join(cur + cur)
        ns = ns[1:]  
        index = ns.find("".join(cur)) + 1  
        lcm = (lcm * index) // gcd(lcm, index)
    
    print(lcm)

t = I()
for _ in range(t):
    solve()
    