# Problem: Anji's Binary Tree - https://codeforces.com/contest/1900/problem/C

from collections import defaultdict
t = int(input())
for _ in range(t):
    n = int(input())
    dire = input()
    ans = []
    graph = defaultdict(int)
    for i in range(n):
        a , b = map(int , input().split())
        graph[i] = [dire[i] , a-1 , b-1]
    stack = []
    stack.append([0,0])
    while stack:
        node = stack.pop()
        if graph[node[0]][1] == -1 and graph[node[0]][2] == -1:
            ans.append(node[1])
        elif graph[node[0]][0] == "L":
            if graph[node[0]][2] != -1:
                stack.append([graph[node[0]][2], node[1] + 1])
            if graph[node[0]][1] != -1:
                stack.append([graph[node[0]][1], node[1]])
        elif graph[node[0]][0] == "R":
            if graph[node[0]][2] != -1:
                stack.append([graph[node[0]][2], node[1]])
            if graph[node[0]][1] != -1:
                stack.append([graph[node[0]][1], node[1] + 1])
        elif graph[node[0]][0] == "U":
            if graph[node[0]][2] != -1:
                stack.append([graph[node[0]][2], node[1] + 1])
            if graph[node[0]][1] != -1:
                stack.append([graph[node[0]][1], node[1] + 1])
        
    print(min(ans))
