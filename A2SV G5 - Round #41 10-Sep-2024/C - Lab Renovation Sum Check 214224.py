# Problem: C - Lab Renovation Sum Check - https://codeforces.com/gym/545013/problem/C


n = int(input())
a = [list(map(int, input().split())) for _ in range(n)]
def check(x, y):
    for i in range(n):
        for j in range(n):
            if i != x and j != y and a[i][y] + a[x][j] == a[x][y]:
                return True
    return False
for i in range(n):
    for j in range(n):
        if a[i][j] != 1 and not check(i, j):
            print("No")
            exit()
print("Yes")