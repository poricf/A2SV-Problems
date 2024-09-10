# Problem: E - Blocking Paths for Safe Escape - https://codeforces.com/gym/515998/problem/E

import sys
from collections import defaultdict, deque

sys.setrecursionlimit(10**3)
INF = float('inf')
N = 10**5 + 10

def I(): return int(sys.stdin.readline().strip())
def ILT(): return list(map(int, sys.stdin.readline().strip().split()))
def S(): return sys.stdin.readline().strip()
def SLT(): return sys.stdin.readline().strip().split()
def DIG(): return [int(i) for i in (list(sys.stdin.readline().strip()))]
def CHAR(): return list(sys.stdin.readline().strip())
ORD = lambda: [ord(char) for char in sys.stdin.readline().strip()]

def solve():
    n, m = ILT()
    graph = [list(S()) for _ in range(n)]
    
    dirx = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    good, bad, empty = [], [], []

    for row in range(n):
        for col in range(m):
            if graph[row][col] == 'G':
                good.append((row, col))
            elif graph[row][col] == 'B':
                bad.append((row, col))
            elif graph[row][col] == '.':
                empty.append((row, col))

    for row, col in empty:
        for i, j in dirx:
            _row, _col = row + i, col + j
            if 0 <= _row < n and 0 <= _col < m and graph[_row][_col] == 'B':
                graph[row][col] = '#'
                break 

    in_bound = lambda i, j: 0 <= i < n and 0 <= j < m

    stack = [(n - 1, m - 1)]
    visited = set()
    
    while stack:
        row, col = stack.pop()
        if not in_bound(row, col) or (row, col) in visited or graph[row][col] == '#':
            continue
        visited.add((row, col))
        for i, j in dirx:
            _row, _col = row + i, col + j
            stack.append((_row, _col))

    ans = 'Yes'
    
    for cell in good:
        if cell not in visited:
            ans = 'No'
            break
        
    for cell in bad:
        if cell in visited:
            ans = 'No'
            break

    print(ans)


for _ in range(I()):
    solve()