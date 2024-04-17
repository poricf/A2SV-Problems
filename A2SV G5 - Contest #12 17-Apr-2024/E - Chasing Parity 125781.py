# Problem: E - Chasing Parity - https://codeforces.com/gym/517685/problem/E

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
    nums = ILT()
    ans = [-1] * n
    graph = defaultdict(list)
    q = deque()
    for i,num in enumerate(nums):
        left , right = i - num, i + num
        
        if (0 <= left < n and (nums[left] + num) % 2 ) or (0 <= right < n and (nums[right] + num) % 2):
            ans[i] = 1
        if right < n and ((nums[right] + nums[i])%2!=0):
            ans[i] = 1
        if ans[i] == 1:
            q.append(i)
        else:
            if 0 <= left < n:
                graph[left].append(i)
            if 0 <= right < n:
                graph[right].append(i)
    while q:
        i = q.popleft()
        for neighbour in graph[i]:
            if ans[neighbour] == -1:
                ans[neighbour] = ans[i] + 1
                q.append(neighbour)
    print(*ans)


# for _ in range(I()):
solve()