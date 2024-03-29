from collections import *
from bisect import *
from itertools import *


MOD = 10**9 + 7



############ ---- Input Functions ---- ############

def inp():
    return(int(input()))
def inlt():
    return(list(map(int,input().split())))
def insr():
    s = input()
    return(list(s))
def insint():
    s = input()
    return([int(x) for x in s])
    
def invr():
    return(map(int,input().split()))
N = (100) + 2
####################################################

def nsum(n):
    return (n*(n+1))//2

'''
    5 7 8  11   12  100
    2 7 2   2   12  13

    4-5,
4 5
1 7
7 8
10 11
1 12
88 100/

3 4
3 3

[]

rang = [1 7,10,1...]
    start from max 
    then cover all 

    sorted h = 2-0 , 2-2 , 2-3 , 7-1 , 12-4 , 13-5

    

'''
def solve():
    n = inp()
    k = inlt()
    h = inlt()

    st = []

    rn = 0

    for i in range(n):
        si = k[i] - h[i]
        ei = k[i]
        

        
        while (st and si <= st[-1][0]):
            st.pop()



        if st and si < st[-1][1] and si > st[-1][0]:
            l,r = st.pop()
            st.append((l,ei))
        else:
            st.append((si,ei))


    for i in range(len(st)):
        ans += nsum(st[i][1] - st[i][0])

    print(ans)

        

        
    
        
for _ in range(inp()):
    solve()