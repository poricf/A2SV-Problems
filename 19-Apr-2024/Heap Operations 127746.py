# Problem: Heap Operations - https://codeforces.com/contest/681/problem/C

######################################################################
###########     Author - Fahmi Dinsefa                  ##############
###########     Created at 4/8/2024                     ############## 
######################################################################

import sys; sys.setrecursionlimit(10**3); INF = float('inf'); N = 10**5 + 10; alpha = '/abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ/'; I = lambda: int(sys.stdin.readline().strip()); ILT = lambda: list(map(int, sys.stdin.readline().strip().split())); S = lambda: sys.stdin.readline().strip(); SLT = lambda: sys.stdin.readline().strip().split(); DIG = lambda: [int(i) for i in (list(sys.stdin.readline().strip()))]; CHAR = lambda: list(sys.stdin.readline().strip()); ORD = lambda: [ord(char) for char in sys.stdin.readline().strip()]; from collections import Counter, defaultdict, deque; from bisect import bisect_right, bisect_left; from math import ceil, sqrt, gcd; from heapq import heapify, heappop, heapreplace, heappush




instructions = []
heap = []


def remove():
    if heap:
        heappop(heap)
    else:
        instructions.append("insert 0")
        
    instructions.append('removeMin')

def insert(num):
    val = int(num)

    heappush(heap, val)
    instructions.append(f"insert {val}")

def getmin(num):
    val = int(num)
    while heap and val > heap[0]:
        remove()
    
    if heap and heap[0] != val:
        insert(val)
    elif not heap:
        insert(val)

    instructions.append(f"getMin {heap[0]}")




for _ in range(I()):
    command = SLT()
    if command[0] == "insert":
        insert(command[1])
    elif command[0] == "getMin":
        getmin(command[1])
    else:
        remove()

    
print(len(instructions))
for inst in instructions:
    print(inst)


                



