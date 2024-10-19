# Problem: Divide and equalize - https://codeforces.com/problemset/problem/1881/D


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
import math
from functools import reduce




ss = set()
def ssr(size):
    half = ''.join(chr(ord('1') + i) for i in range((size // 2) + 1))
    return half + half[-2::-1]


def precalculate():
    s = "1"
    while len(s) < 17:
        ss.add(s)
        for i in range(len(s)):
            if s[i] == '9':
                s = ssr(len(s) + 2)
                break
            s = s[:i] + chr(ord(s[i]) + 1) + s[i+1:]

precalculate()

def gcd(a, b):
    return a if b == 0 else gcd(b, a % b)

def calc(s):
    return reduce(lambda sum, char: sum * 10 + ord(char) - ord('0'), s, 0)

def solve(k):
    a, b, m =ILT()
    ans = sum(1 for it in ss if a <= (num := calc(it)) <= b and num % m == 0)
    print(f"Case #{k}:",ans)

t = I()
for _ in range(t):

    solve(_+1)
