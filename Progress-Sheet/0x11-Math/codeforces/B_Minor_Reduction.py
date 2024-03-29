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


'''
    2
    if sm > 10  use that 
    else add the last 2

    time limit exceded

    start from right

    10099
    10018

    10057
    10012

    x[i-1] = 1
    x[i] =  9 + 8 + 1



'''

def solve():
    s = insint()
    s = deque(s)
    n = len(s)
    ans = []
    flag = 0
    for i in range(n-2,-1,-1):
        sm = s[i] + s[i+1]
        if sm >= 10:
            s[i+1] = s[i] + s[i+1] - 10
            s[i] = 1
            flag = 1
            print("".join(map(str,s)))
            return
    
    s[1] = s[0] + s[1]
    s.popleft() 
    print("".join(map(str,s)))

            
    
    
        
for _ in range(inp()):
    solve()