# Problem: D - Medina & Merbebt - https://codeforces.com/gym/522079/problem/D

######################################################################
###########     Author - Fahmi Dinsefa                  ##############
###########     Created at 4/8/2024                     ############## 
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




def solve():
    n = I()
    nums = ILT()
    q = I()

    a = [0] * 32
    pref = [a]

    for num in nums:
        a = pref[-1].copy()
        for i in range(32):
            if num & (1 << i) != 0:
                a[i] += 1
        pref.append(a)

    def check(l, r):
        ans = 0
        for i in range(32):
            bit_count = pref[r][i] - pref[l - 1][i] if l > 0 else pref[r][i]
            if bit_count == (r - l + 1):
                ans |= (1 << i)
        return ans

    def BS(l, k):
        left = l
        right = n
        while left <= right:
            mid = (right + left) // 2
            if check(l, mid) >= k:
                left = mid + 1
            else:
                right = mid - 1

        if right < l:
            return -1
        return right

    ans = []
    for _ in range(q):
        l, k = map(int, input().split())
        ans.append(BS(l, k))

    print(*ans)



for _ in range(I()):
    solve()

