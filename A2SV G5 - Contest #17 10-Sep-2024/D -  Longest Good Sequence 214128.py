# Problem: D -  Longest Good Sequence - https://codeforces.com/gym/524965/problem/D


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
from heapq import heapify, heappop, heapreplace, heappush



import sys
sys.setrecursionlimit(10**3)
INF = float('inf')
NINF = float('-inf')

N = 10**5 + 10
alpha = '/abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ/' 
MOD = 10**9 + 1

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
import math

def Gsum(a, r, n):
    if n == INF:
        return a/(1-r)
    elif r == 1:
        return a * n
    else:
        return a * (1 - r**n) / (1 - r)


def prime_factors(n):
    factors = []
    while n % 2 == 0:
        factors.append(2)
        n //= 2
    sqrt_n = math.isqrt(n)
    for i in range(3, sqrt_n + 1, 2):
        while n % i == 0:
            factors.append(i)
            n //= i
    if n > 2:
        factors.append(n)
    return factors


def sieve(n):
    if n < 2:
        return []
    primes = [True] * (n + 1)
    primes[0] = primes[1] = False
    sqrt_n = math.isqrt(n)
    for i in range(2, sqrt_n + 1):
        if primes[i]:
            for j in range(i * i, n + 1, i):
                primes[j] = False
    return [i for i in range(n + 1) if primes[i]]


def factors(n):
    if n <= 0:
        return []
    sqrt_n = math.isqrt(n)
    factors = []
    for i in range(2, sqrt_n + 1):
        if n % i == 0:
            factors.append(i)
            if i != n // i:
                factors.append(n // i)
    return factors 

def is_prime(n):
    if n < 2:
        return False
    sqrt_n = math.isqrt(n)
    for i in range(2, sqrt_n + 1):
        if n % i == 0:
            return False
    return True

def modexp(base, exponent, MOD):
    result = 1
    base = base % MOD

    while exponent > 0:
        if exponent % 2 == 1:
            result = (result * base) % MOD
        exponent = exponent // 2
        base = (base * base) % MOD

    return result


def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a


def lcm(a, b):
    return abs(a * b) // gcd(a, b)



def solve():
    

    n = I()

    a = ILT()

    if n == 1 and a[0] == 1:
        print(1)
        return
 


    dp = [0] *(max(a) + 1)

    for num in a:
        fac = factors(num)
        dp[num] = 1
        for div in fac:
            dp[num] = max(dp[num], dp[div] + 1)

        for div in fac:
            dp[div] = max(dp[div], dp[num])
    print(max(dp))

# for _ in range(I()):
solve()