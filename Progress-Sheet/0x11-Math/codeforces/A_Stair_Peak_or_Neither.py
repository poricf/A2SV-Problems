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
N = (100) + 2

prime = [0] * N


def solve(): 
    a = inlt()
    

    if a[0] < a[1] and a[1] < a[2]:
        print("STAIR")
    elif a[1] > a[0] and a[1] > a[2] or a[1]> a[0] and a[1] > a[2]:
        print("PEAK")
    else:
        print("NONE")


            
    
for _ in range(inp()):
    solve()