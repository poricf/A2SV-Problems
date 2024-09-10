# Problem: Turtle vs. Rabbit Race: Optimal Trainings - https://codeforces.com/contest/1933/problem/E


import sys

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





def calc(m, u, l):
    s = pref[m + 1] - pref[l - 1]
    return (s * (2 * u - s + 1)) / 2



for i in range(I()):
    n = I()
    a = ILT()

    pref = [0]
    for num in a:
        pref.append(pref[-1] + num)

    result = []

    for j in range(I()):

        l, u = ILT()

        left = l - 1
        right = n - 1

        ans = right

        while left <= right:
            mid = (left + right) // 2
            
            s = pref[mid + 1] - pref[l - 1]
            
            if s >= u:
                ans = mid
                right = mid - 1
            
            else:
                left = mid + 1

        if ans > l - 1 and calc(ans - 1, u, l) >= calc(ans, u, l):
            ans -= 1

        result.append(ans + 1)

    print(*result)
    
