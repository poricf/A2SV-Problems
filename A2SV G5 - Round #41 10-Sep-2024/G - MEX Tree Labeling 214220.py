# Problem: G - MEX Tree Labeling - https://codeforces.com/gym/544853/problem/E







def solve():
    n = int(input())
    d = [0] * (n + 1)
    edges = [[0, 0] for _ in range(n - 1)]
    for i in range(n - 1):
        u, v = map(int, input().split())
        edges[i][0] = u
        edges[i][1] = v
        d[u] += 1
        d[v] += 1
    # print(d)
    left = 0
    right = n - 2

    for x, y in edges:
        if d[x] == 1 or d[y] == 1:
            print(left)
            left += 1
        else:
            print(right)
            right -= 1


# for _ in range(I()):
solve()