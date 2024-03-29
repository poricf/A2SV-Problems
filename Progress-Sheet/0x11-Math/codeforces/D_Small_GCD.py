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

for i in range(2,N):
    if not prime[i]:
        prime[i] = i

        for j in range(i*i,N,i):
            if not prime[j]:
                prime[j]

print(prime)

def solve():  
    n = inp()
    a = inlt()
            
    
for _ in range(inp()):
    solve()