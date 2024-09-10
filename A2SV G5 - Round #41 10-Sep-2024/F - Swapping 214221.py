# Problem: F - Swapping - https://codeforces.com/gym/544853/problem/D


for _ in range(int(input())):
	n,x,m= list(map(int,input().split()))
	a,b=x,x
	for i in range(m):
		l , r = list(map(int,input().split()))
		if b >= l and a <= r:
			a = min(l,a)
			b = max(b,r)
	print(b-a+1)
