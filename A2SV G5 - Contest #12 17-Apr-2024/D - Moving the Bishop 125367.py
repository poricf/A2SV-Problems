# Problem: D - Moving the Bishop - https://codeforces.com/gym/517685/problem/D

######################################################################
###########     Author - Fahmi Dinsefa                  ##############
###########     Created at 4/8/2024                     ############## 
######################################################################

import sys
sys.setrecursionlimit(10**3)
INF = float('inf')
N = 10**5 + 10
alpha = '/abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ/' 

def inp(): return int(sys.stdin.readline().strip())
def inlt(): return list(map(int, sys.stdin.readline().strip().split()))
def String(): return sys.stdin.readline().strip()
def Slist(): return sys.stdin.readline().strip().split()
def Digit(): return [int(i) for i in (list(sys.stdin.readline().strip()))]
def Char(): return list(sys.stdin.readline().strip())
ORD = lambda: [ord(char) for char in sys.stdin.readline().strip()]
def dbg(*args): print(args)

from collections import Counter, defaultdict, deque
from bisect import bisect_right, bisect_left
from math import ceil, sqrt, gcd



def solve():

    n = inp()
    ax, ay = inlt()
    bx, by = inlt()
    grid = []
    for _ in range(n):
        row = input()
        grid.append(row)



    ans = 0

    in_bound = lambda i, j: 0 <= i < len(grid) and 0 <= j < len(grid[0])
    directions = [(1, 1), (1, -1), (-1, 1), (-1, -1)]
    q = deque([(ax-1, ay-1)])
    visited = {1: set(), -1: set()}
    while q:
        # dbg(q)
        # dbg(visited)
        for _ in range(len(q)):
            x, y = q.popleft()
            if x == bx-1 and y == by-1:
                print(ans)
                return
                
            
            for dx, dy in directions:
                new_x, new_y = x + dx, y + dy

                while in_bound(new_x,new_y) and (new_x,new_y) not in visited[dx*dy] and grid[new_x][new_y] == ".":
                    q.append((new_x, new_y))
                    visited[dx*dy].add((new_x, new_y))
                    
                    new_x += dx
                    new_y += dy
        ans += 1
        
    print(-1)

solve()


