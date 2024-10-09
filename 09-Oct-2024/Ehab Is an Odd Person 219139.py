# Problem: Ehab Is an Odd Person - https://codeforces.com/problemset/problem/1174/B

n=int(input())
a=list(map(int,input().split()))
for i in a:
    if((i+a[0])%2):
        a.sort()
        break
print(*a)