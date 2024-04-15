# Problem: They Are Everywhere - https://codeforces.com/problemset/problem/701/C

######################################################################
###########     Author - Fahmi Dinsefa                  ##############
###########     Created at 4/8/2024                     ############## 
######################################################################

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
    s = S()
    target = len(set(s))

    ans = len(s)
    window = defaultdict(int)
    l,r = 0,0
    while r < n:
        window[s[r]] += 1

        if len(window) == target:
            while len(window) == target:
                ans = min(ans, r-l+1)
                window[s[l]] -= 1
                
                if window[s[l]] == 0:
                    del window[s[l]]
                l += 1
                    
        r += 1
    print(ans)




# for _ in range(I()):
solve()