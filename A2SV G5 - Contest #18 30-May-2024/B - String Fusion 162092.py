# Problem: B - String Fusion - https://codeforces.com/gym/526229/problem/B

######################################################################
###########     Author - Fahmi Dinsefa                  ##############
###########     Created at 5/25/2024                     ############## 
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
from heapq import heapify, heappop, heapreplace, heappush


def add(x):
    global len_hmap
    p = 0
    for c in x:
        ind = ord(c) - ord('a')
        if not hmap[p][ind]:
            hmap[p][ind] = len_hmap
            len_hmap += 1
        p = hmap[p][ind]
        cnt[p] += 1


N = 1000005
n, sum, ans = 0, 0, 0
hmap = [[0] * 26 for _ in range(N)]
cnt = [0] * N
len_hmap = 1
s = []


n = I()
for i in range(1, n + 1):
    t = S()
    s.append(t)
    add(t)

    print()
    sum += len(t)


for i in range(n):
    sn = len(s[i])
    ans += sum + sn * n
    p = 0
    for j in range(sn - 1, -1, -1):
        ind = ord(s[i][j]) - ord('a')
        if not hmap[p][ind]:
            break
        p = hmap[p][ind]
        ans -= cnt[p] * 2
print(ans)



# for _ in range(I()):
# # solve()
# def fusion(a,b):
#     la = len(a)
#     lb = len(b)
#     aa = a[::-1]
#     res = la + lb
#     # print(la,lb)
#     for i in range(min(la,lb)):
#         if aa[i] == b[i]:
#             res -= 2
        
            

    
#     return res
# sum = 0
# s = []
# n = I()
# for i in range(n):
#     t = S()
#     s.append(t)
#     sum += len(t)
# # print(sum)
# ans = 0
# for i in range(n):
#     for j in range(n):
#         # print(s[i],s[j],fusion(s[i],s[j]))

#         ans += fusion(s[i],s[j])

# print(ans)




