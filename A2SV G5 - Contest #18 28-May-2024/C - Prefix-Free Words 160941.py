# Problem: C - Prefix-Free Words - https://codeforces.com/gym/526229/problem/C

######################################################################
###########     Author - Fahmi Dinsefa                  ##############
###########     Created at 5/25/2024                     ############## 
######################################################################
class Trie:
    def __init__(self):
        self.root = TrieNode()
    

    def insert(self,word):
        cur = self.root
        for c in word:
            ind = ord(c) - oa
            if cur.children[ind] is None:
                cur.children[ind] = TrieNode()

            cur = cur.children[ind]
        cur.end = True



    def search(self, word):
        cur = self.root
        for c in word:
            index = ord(c) - ord('a')
            if cur.children[index] is None:
                return False
            cur = cur.children[index]
        return cur.is_end

    def startsWith(self, prefix: str) -> bool:
        cur = self.root
        for c in prefix:
            index = ord(c) - ord('a')
            if cur.children[index] is None:
                return False
            cur = cur.children[index]
        return True

    def delete(self, word):
        def _delete(cur, word, index):
            if index == len(word):
                if not cur.is_end:
                    return False
                cur.is_end = False
                return len([child for child in cur.children if child is not None]) == 0
            
            c_ind = ord(word[index]) - ord('a')
            child_cur = cur.children[c_ind]
            if child_cur is None:
                return False
            
            shoud_delett = _delete(child_cur, word, index + 1)
            if shoud_delett:
                cur.children[c_ind] = None
                return len([child for child in cur.children if child is not None]) == 0 and not cur.is_end
            
            return False
        
        return _delete(self.root, word, 0)

import sys
sys.setrecursionlimit(10**3)
INF = float('inf')
N = 10**5 + 10
alpha = '/abcdefghijklposopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ/' 

def I(): return int(sys.stdin.readline().strip())
def ILT(): return list(map(int, sys.stdin.readline().strip().split()))
def S(): return sys.stdin.readline().strip()
def SLT(): return sys.stdin.readline().strip().split()
def DIG(): return [int(i) for i in (list(sys.stdin.readline().strip()))]
def CHAR(): return list(sys.stdin.readline().strip())
def jj(elem): return ("".join(map(str, elem)))
ORD = lambda: [ord(char) for char in sys.stdin.readline().strip()]


from collections import Counter, defaultdict, deque
from bisect import bisect_right, bisect_left
from math import ceil, sqrt, gcd
from heapq import heapify, heappop, heapreplace, heappush




def solve():
    n = I()
    a = ILT()
    sz = [(a[i], i) for i in range(n)]
    sz.sort()
    pos = [0]
    ans = [""] * n
    for j in range(n):
        a, b = sz[j]
        
    
        while len(pos) < a:
            pos.append(0)

        ans[b] = jj(pos)
        pos[-1] += 1
        for i in range(len(pos) - 1, -1, -1):
            if pos[i] == 2:
                pos[i] = 0
                if i - 1 < 0 and j != n - 1:
                    print("NO")
                    return
                pos[i - 1] += 1
                print(pos)
    print("YES")
    for x in ans:
        print(x)

# for _ in range(I()):
solve()

