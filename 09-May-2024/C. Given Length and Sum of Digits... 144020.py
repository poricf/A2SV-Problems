# Problem: C. Given Length and Sum of Digits... - https://codeforces.com/contest/489/problem/C

def solve():
    n, s = map(int, input().split())
    mx = ""
    mn = ""
    if s == 0:
        if n == 1:
            print(0 ,0)
        else:
            print(-1, -1)
        return
    for i in range(n):
        a = min(9, s)
        mx += str(a)
        s -= a

    for i in range(n - 1, -1, -1):
        mn += mx[i]
    mn = list(mn)
    if s > 0:
        print(-1,-1)
        return
    if mn[0] == '0':

        # print("hey")
        for i in range(len(mn)):
            if mn[i] != '0':
                mn[i] = str(int(mn[i])-1)
                mn[0] = '1'
                break
    
    

    print("".join(mn),mx)

solve()