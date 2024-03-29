from collections import *
from bisect import *
from itertools import *


MOD = 10**9 + 7



############ ---- Input Functions ---- ############
def inp():
    return(int(input()))
def inlt():
    return(list(map(int,input().split())))
def insr():
    s = input()
    return(list(s))
def invr():
    return(map(int,input().split()))
N = 100010
##############################################



fact = [[] for i in range(N)]
a = [0] * N
ct = [0] * N
b = [0] * N

#store factors of all integers upto 10 ** 4
for i in range(1,N):
    for j in range(i,N,i):
        fact[j].append(i)
    fact[i].reverse()

# print(fact)

def solve():
    n = inp()
    z = inlt()
    for j in range(0,len(z)):
        a[j] = z[j]
    a[:n] = sorted(a[:n])


    ans = 0
    cur = 0
    ct = [0] * N
    for i in range(n):
        ans += cur 
        for x in fact[a[i]]:
            b[x] = ct[x]

            for y in fact[a[i]]:
                if y <= x:
                    break
                elif y % x == 0:
                    b[x] -= b[y]
            cur += x * b[x]
        for x in fact[a[i]]:
            ct[x] += 1
    print(ans)


for _ in range(inp()):
    solve()