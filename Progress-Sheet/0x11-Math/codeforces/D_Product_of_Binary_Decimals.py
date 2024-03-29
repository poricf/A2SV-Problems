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
N = (10**5) + 2
bd = []

i = 2
######################################
while i < N:
    num = i
    flag = True
    while num > 0:
        if num % 10 > 1:
            flag = False
            break
        
        num //=10
    
    if flag:
        bd.append(i)
    i+=1
#############################


def rec(n):
    if n == 1:
        return True
    ans = 0
    for d in bd:
        if n % d == 0:
            ans = ans or rec(n//d)
    
    return ans


def solve(): 
    n = inp()
    print("YES" if rec(n) else "NO")
    

    

for _ in range(inp()):
    solve()