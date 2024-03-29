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
    a , b= [int(x) for x in input().split(":")]   
    # print(a,b)
    if b < 10:
        b = "0" + str(b)
    b = str(b)
    hr = 0
    if a > 12:
        suf = "PM"
        hr = a - 12
        if hr < 10:
            hr = "0" + str(hr)
    elif a == 0:
        hr = 12
        suf = "AM"
    elif a == 12:
        hr = 12
        suf = "PM"
    else:

        hr = a
        if hr < 10:
            hr = "0" + str(hr)
        suf = "AM"
    hr = str(hr)
    print(hr + ":" + b,suf)
for _ in range(inp()):
    solve()