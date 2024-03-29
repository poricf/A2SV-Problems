from collections import Counter,defaultdict
def solve(m):
    pfactors = defaultdict(int)
    i = 2
    while i*i <= m:
        while m % i == 0:
            m = m // i
            pfactors[i] +=1

        i+=1
        
    
    if(m>1):  pfactors[m] += 1
    return len(pfactors) == 2



n = int(input())
cnt = 0
for k in range(1,n+1):
    if solve(k):
        cnt+=1

print(cnt)