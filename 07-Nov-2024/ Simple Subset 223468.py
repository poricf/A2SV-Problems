# Problem:  Simple Subset - https://codeforces.com/contest/665/problem/D

import sys
import random

sys.setrecursionlimit(10**3)
N = 1010
X = 2100300

def I(): return int(sys.stdin.readline().strip())
def ILT(): return list(map(int, sys.stdin.readline().strip().split()))

def solve():
    n = I()
    a = ILT()
    
    seive = [0] * X
    p = []
    for i in range(2, X):
        if seive[i] == 0:
            p.append(i)
            seive[i] = i
        j = 0
        while j < len(p) and p[j] <= seive[i] and i * p[j] < X:
            seive[i * p[j]] = p[j]
            j += 1
    
    cnt1 = a.count(1)
    isPrime = lambda x: seive[x] == x
    
    if cnt1 > 0:
        # Case 1: Find a non-1 element that can form a prime with a `1`
        for x in a:
            if x != 1 and isPrime(x + 1):
                ans = [1] * cnt1 + [x]
                print(len(ans))
                print(*ans)
                return

        # Case 2: If there are more than one `1`s, we can just return them
        if cnt1 > 1:
            ans = [1] * cnt1
            print(len(ans))
            print(*ans)
            return
    
    # Case 3: Try finding any pair (not involving `1`) that forms a prime sum
    for i in range(n):
        for j in range(i + 1, n):
            if isPrime(a[i] + a[j]):
                ans = [a[i], a[j]]
                print(len(ans))
                print(*ans)
                return
    
    print(1)
    print(a[0])

solve()
