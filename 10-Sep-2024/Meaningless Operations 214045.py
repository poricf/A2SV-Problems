# Problem: Meaningless Operations - https://codeforces.com/problemset/problem/1110/C


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
	if (n + 1) & n:
		print(2 ** (n.bit_length()) - 1)
	else:
		x = 2
		while n % x:
			if x * x > n:
				x = n
				break
			x += 1
		print(n // x)

for _ in range(I()):
    solve()