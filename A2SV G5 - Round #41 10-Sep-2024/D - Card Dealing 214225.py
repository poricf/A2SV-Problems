# Problem: D - Card Dealing - https://codeforces.com/gym/545013/problem/D


def solve():
    n = int(input())
    a = 0
    b = 0
    for i in range (1,n+1):
        if i%4 < 2:
            a += min(i, n)
        else:
            b += min(i, n)
        n-=i
        if(n<=0): 
            break
    print(a, b)

for _ in range(int(input())):
    solve()