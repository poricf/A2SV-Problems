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


'''
2

abcdcba
ababcdc
abcdabc
'''

def solve():  
    s = insr()
    s.sort()
    

    print("".join(s))




    
for _ in range(inp()):
    solve()