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
def insint():
    s = input()
    return([int(x) for x in s])
    
def invr():
    return(map(int,input().split()))
N = (100) + 2
####################################################
def solve():
    a, b, c = invr()
    numEdges = a * 2 + b * 1 + c * 0
    numEdges += 1
    if numEdges != (a + b + c):
        print(-1)
    else:
        cur = c
        ans = 0
        while a != 0 or b != 0:
            if cur <= b:
                b -= cur
                ans += 1
            else:
                thing = cur - b
                if thing % 2 == 0:
                    ans += 1
                    a -= thing // 2
                    b = 0
                    cur -= thing // 2
                else:
                    b = 1
                    a -= (thing // 2 + 1)
                    ans += 1
                    cur -= (thing // 2 + 1)
        print(ans)

t = int(input())
for _ in range(t):
    solve()