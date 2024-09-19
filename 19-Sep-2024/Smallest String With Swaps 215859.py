# Problem: Smallest String With Swaps - https://leetcode.com/problems/smallest-string-with-swaps/

class Solution:
    def smallestStringWithSwaps(self, s: str, pairs: List[List[int]]) -> str:
        djs = DSU(len(s))
        res = ["" for i in range(len(s))]
        for pair in pairs:
            djs.union(pair[0], pair[1])
        
        parent = {}
        p2 = {}
        for i in range(len(s)):
            p = djs.find(i)
            p2[p] = p2.get(p, [])
            parent[p] = parent.get(p, [])
            parent[p].append(i)
            p2[p].append(s[i])
        
        for item in parent:
            parent[item].sort()
        for item in p2:
            p2[item].sort()

        for item in parent:
            x = parent[item]
            y = p2[item]

            for i in range(len(x)):
                res[x[i]] = y[i]

    
        return "".join(res)
        


class DSU:

    def __init__(self,n):
        self.root = [i for i in range(n)]
        self.rank = [0 for i in range(n)]
    

    def find(self, x):
        
        if self.root[x] == x:
            return x
        

        self.root[x] = self.find(self.root[x])
        return self.root[x]
    

    def union(self, a, b):
        A = self.find(a)
        B = self.find(b)

        if self.rank[A] > self.rank[B]:
            self.root[B] = A
        elif self.rank[B] > self.rank[A]:
            self.root[A] = B
        else:
            self.root[A] = B
            self.rank[B] += 1
    

        