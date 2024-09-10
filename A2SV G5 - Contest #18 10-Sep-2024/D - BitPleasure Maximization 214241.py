# Problem: D - BitPleasure Maximization - https://codeforces.com/gym/526229/problem/D


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



class node:
    def __init__(self):
        self.bit_link = [None]*2

  
class Trie:
    def __init__(self):
        self.root = node()


    def insert(self, num):
        cur = self.root

        for i in range(62, -1, -1):
            bit = (num >> i) & 1

            if not cur.bit_link[bit]:
                cur.bit_link[bit] = node()

            cur = cur.bit_link[bit]

    def _max(self, num):
        cur = self.root
        ans = 0

        for i in range(62, -1, -1):
            bit = (num >> i) & 1

            if cur.bit_link[1 - bit]:
                ans = ans | 1 << i
                cur = cur.bit_link[1 - bit]
            else:
                cur = cur.bit_link[bit]

        return ans

def solve():
    n = I()
    nums = ILT()
    trie = Trie()
    cur = 0
    trie.insert(cur)
    for i in range(n):
        cur ^= nums[i]
        trie.insert(cur)
    cur = 0
    ans = 0
    ans = max(ans, trie._max(cur))
    for i in range(n - 1, -1, -1):
        cur ^= nums[i]
        ans = max(ans, trie._max(cur))


    print(ans)

solve()