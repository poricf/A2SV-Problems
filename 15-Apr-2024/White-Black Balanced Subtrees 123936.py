# Problem: White-Black Balanced Subtrees - https://codeforces.com/contest/1676/problem/G

import threading
from sys import stdin,stdout,setrecursionlimit
from collections import defaultdict
import sys

setrecursionlimit(1 << 30)
threading.stack_size(1 << 27)


def input():
    return sys.stdin.readline()

def main():
    t = int(input())
    for _ in range(t):
        n = int(input())
        nums = list(map(int, input().split()))
        color = input()
        graph = defaultdict(list)
        for i in range(len(nums)):
            graph[nums[i]].append(i+2)
        ans = 0

        def dfs(node):
            nonlocal ans
            if node not in graph:
                if color[node-1] == 'B':
                    return[1, 0]
                else:
                    return [0, 1]
                
            rec = [0, 0]
            for i in graph[node]:
                temp = dfs(i)
                rec[0] += temp[0]
                rec[1] += temp[1]
            
            if color[node-1] == 'B':
                rec[0] += 1
            else:
                rec[1] += 1
            
            if rec[0] == rec[1]:
                ans += 1
            
            return rec
        
        dfs(1)
        print(ans)
                
main_thread = threading.Thread(target=main)
main_thread.start()
main_thread.join()