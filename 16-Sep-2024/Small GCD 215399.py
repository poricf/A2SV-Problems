# Problem: Small GCD - https://codeforces.com/contest/1900/problem/D

from collections import *
from bisect import *
from itertools import *
import sys

MOD = 10**9 + 7



############ ---- Input Functions ---- ############
def inp():
    return int(sys.stdin.readline().strip())
def inlt():
    return list(map(int, sys.stdin.readline().strip().split()))
def insr():
    return sys.stdin.readline().strip()
def invr():
    return(map(int,input().split()))
def intstr():
    return [int(i) for i in (list(sys.stdin.readline().strip()))]
N = 100010
##############################################



fact = [[] for i in range(N)]

b = [0] * N
cnt = [0] * N
#store factors of all integers upto 10 ** 4
for i in range(1,N):
    for j in range(i,N,i):
        fact[j].append(i)
for i in range(1,N):
    fact[i].sort(reverse= True)


# print(fact)

def solve():
    n = int(input())
    nums = inlt()
    nums.sort()
    ans = 0
    rem = n
    for num in nums:
        rem -= 1
        for d in fact[num]:
            val = cnt[d] - b[d]
            for d2 in fact[d]:
                b[d2] += val
            ans += d * val * rem

        for d in fact[num]:
            for d2 in fact[d]:
                b[d2] = 0

        for d in fact[num]:
            cnt[d] += 1
    for num in nums:
        for d in fact[num]:
            cnt[d] = 0
    print(ans)


for _ in range(inp()):
    solve()