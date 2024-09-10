# Problem: E - Min Divisible Outside Segment - https://codeforces.com/gym/545013/problem/E


def solve():
    l , r , d = map(int,input().split())
   
    if d < l or d > r:
        print(d)
    else:
        ch = l % d
        cz = r % d
        ans1 = r - cz + d
        print(ans1)







for _ in range(int(input())):
    solve()