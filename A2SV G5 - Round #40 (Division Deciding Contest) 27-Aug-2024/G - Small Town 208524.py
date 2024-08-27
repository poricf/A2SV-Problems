# Problem: G - Small Town - https://codeforces.com/gym/543431/problem/G

import sys
sys.setrecursionlimit(10**3)
INF = float('inf')
N = 10**5 + 10
alpha = '/abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ/' 

def I(): return int(sys.stdin.readline().strip())
def ILT(): return list(map(int, sys.stdin.readline().strip().split()))
def S(): return sys.stdin.readline().strip()
def SLT(): return sys.stdin.readline().strip().split()
def DIG(): return [int(i) for i in (list(sys.stdin.readline().strip()))]
def CHAR(): return list(sys.stdin.readline().strip())
ORD = lambda: [ord(char) for char in sys.stdin.readline().strip()]


from collections import Counter, defaultdict, deque
from bisect import bisect_right, bisect_left
from math import ceil, sqrt, gcd




def solve():
    n = I()
    a = ILT()
    a.sort()

    def check(m):

        first = a[0]
        i = 0

        while i < n and ((abs(first - a[i]))/2 )<= m:
             i+=1
        
        if i < n: 
            second = a[i]

            while i < n and (abs(second - a[i])/2) <= m:
                i += 1
       
        if i < n:
            third = a[i]

            while i < n and (abs(third - a[i])/2) <= m:
                i += 1

        

        return i == n

            
        

        

    
    l = 0 ; r = 10 ** 9
    # l = r = 0
    best = -1

    while l <= r:
        m = (l+r) // 2

        if check(m):
            r = m - 1
            best = m
        else:
            l = m + 1
        
    print(best)

for _ in range(I()):
    solve()


    

