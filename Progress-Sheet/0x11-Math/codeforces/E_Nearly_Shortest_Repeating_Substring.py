from collections import *
from bisect import *
from itertools import *

def string_diff(str1, str2):
    res = ""
    for c1, c2 in zip(str1, str2):
        diff = ord(c2) - ord(c1)
        res += str(diff)
    return len(str1) - res.count('0')

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


def solve(): 
    n = inp()
    s = input()
    a = []
    
    if n % 2:
        print(len(s))
        return
    for i in range(1,len(s)+1):
        if n % i == 0:
            nw = s[:i]
            sss = nw*(n//i)
            if string_diff(sss,s) <= 1:
                print(i)
                return
            nw = s[n-i:]
        
            sss = nw*(n//i)
            if string_diff(sss,s) <= 1:
                print(i)
                return
    


for _ in range(inp()):
    solve()