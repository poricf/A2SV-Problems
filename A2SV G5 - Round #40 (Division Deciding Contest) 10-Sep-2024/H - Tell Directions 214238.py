# Problem: H - Tell Directions - https://codeforces.com/gym/543431/problem/H

import sys
from collections import deque

sys.setrecursionlimit(10**3)
INF = float('inf')

def I(): return int(sys.stdin.readline().strip())
def ILT(): return list(map(int, sys.stdin.readline().strip().split()))
def S(): return sys.stdin.readline().strip()

def solve():
    n, m, k = ILT()
    mat = []
    start = []
    for i in range(n):
        row = S()
        if 'X' in row:
            start = [i, row.find('X')]
        mat.append(row)

    if k % 2 != 0:
        print("IMPOSSIBLE")
        return
    
    dist = [[-1 for _ in range(m)] for _ in range(n)]
    dist[start[0]][start[1]] = 0
    dirs = [(1, 0), (0, -1), (0, 1), (-1, 0)]
    possible = lambda i, j: 0 <= i < n and 0 <= j < m and mat[i][j] != '*' 

    def bfs():
        q = deque([start])
        d = 1
        while q:
            for _ in range(len(q)):
                ci, cj = q.popleft()
                for di, dj in dirs:
                    newi, newj = ci + di, cj + dj
                    if possible(newi, newj) and dist[newi][newj] == -1:
                        dist[newi][newj] = d
                        q.append([newi, newj])
            d += 1
        
    bfs()
    symbols = 'DLRU'
    answer = []
    c = 0
    while c < k:
        changed = False
        for i in range(4):
            di, dj = dirs[i]
            ci, cj = start
            if possible(ci + di, cj + dj) and dist[ci + di][cj + dj] <= k - c:
                c += 1
                changed = True
                answer.append(symbols[i])
                start = [ci + di, cj + dj] 
                break
            
        if not changed:
            break
            
    if len(answer) != k:
        print("IMPOSSIBLE")
    else:
        print(''.join(answer))

# for _ in range(I()):
solve()