# Problem: B - Empress Taytu and The Water Source - https://codeforces.com/gym/513152/problem/B

from collections import *
from bisect import *
from itertools import *
from math import *
import sys
input = sys.stdin.readline



############ ---- Input Functions ---- ############
def inp():
    return(int(input()))
def inlt():
    return(list(map(int,input().split())))
def insr():
    s = input()
    return(list(s[:len(s) - 1]))
def invr():
    return(map(int,input().split()))



    

def solve():
    def check(m):
        ct = 0
        for i in range(len(d)):
            ct += (ceil(d[i]/m) * a[i])  
        
        return ct <= k
    

    n , k = invr()
    d = inlt()
    a = inlt()

    l = 1

    r = 10 ** 18
    best = -1
    while l <= r:
        m = (l+r)//2

        if check(m):
            r = m - 1
            best = m
        else:
            l = m + 1
            
            
        
    print(best)
        


# t = 1
t = inp()

for i in range(t):
    solve()
