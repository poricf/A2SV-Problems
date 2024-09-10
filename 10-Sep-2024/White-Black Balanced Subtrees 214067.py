# Problem: White-Black Balanced Subtrees - https://codeforces.com/contest/1676/problem/G

import threading
from sys import setrecursionlimit
import sys

setrecursionlimit(1 << 30)
threading.stack_size(1 << 27)

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





def main():
    # t = 1
    t = I()
    for _ in range(t):
        n = I()
        a = [0,0]  + ILT()
        s = '*' + S()
        graph = defaultdict(list)
        for i in range(2,n+1):
            graph[a[i]].append(i)
        
        ans = [0]

        # print(graph)

        def dfs(node):
            res = [0,0]
            if node not in graph:
                return [(s[node] == 'W') , (s[node] == 'B')]
            for child in graph[node]:
                temp = dfs(child)
                res[0] += temp[0]
                res[1] += temp[1]
            
            res[0] += (s[node] == 'W')
            res[1] += (s[node] == 'B')

            if res[0] == res[1]:
                ans[0] += 1
            

            return res
    


        dfs(1)

        # print(res)

        print(ans[0])

            
                
main_thread = threading.Thread(target=main)
main_thread.start()
main_thread.join()