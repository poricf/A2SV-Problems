# Problem: E - Game is Game - https://codeforces.com/gym/527294/problem/E


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
        self.children = [None]*26


class Trie:
    def __init__(self):
        self.root = node()


    def insert(self, word):
        curr = self.root

        for ch in word:
            idx = ord(ch) - ord('a')
            if not curr.children[idx]:
                curr.children[idx] = node()
            curr = curr.children[idx]

    def canWin(self, ptr):

        for child in ptr.children:
            if child:
                if not self.canWin(child):
                    return True

        return False

    def lose(self, ptr):
        flag = True

        for child in ptr.children:
            if child:
                if self.lose(child):
                    flag = False
                else:
                    return True

        return flag

    def winer(self):
        return (self.canWin(self.root), self.lose(self.root))


def solve():
    n, k = ILT()
    trie = Trie()


    for i in range(n):
        trie.insert(input())

    first, second = trie.winer()
    print("First" if first and (k % 2 or not second) else "Second")

solve()

