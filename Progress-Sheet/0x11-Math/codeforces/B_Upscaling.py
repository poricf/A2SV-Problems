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
    n = inp()
    hashh = "##"
    dot = ".."
    switch = True
    cnt = 0
    for i in range(2*n):
        cnt += 1
        for j in range(n):
            if switch:
                if j % 2 == 0: print(hashh,end = "")
                else: print(dot,end = "")
                
            else:
                if j %2 == 0: print(dot, end = "") 
                else: print(hashh, end = "")
                
        print()
        if cnt == 2:
            cnt = 0
            switch = not switch

        



            
    
for _ in range(inp()):
    solve()