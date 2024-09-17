# Problem: C. Given Length and Sum of Digits... - https://codeforces.com/contest/489/problem/C

m,s = map(int, input().split())
if s > 9 * m or (m > 1 and s == 0):
    print(-1, -1)
elif m == 1:
    print(s, s)
else:
    x, y= 10**(m-1), 0
    for i in range(s - 1):
        x += 10**(i//9)
    for i in range(s):
        y += 10**(m-1-i//9)
    print(x,y)