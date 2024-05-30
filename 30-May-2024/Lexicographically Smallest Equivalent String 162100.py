# Problem: Lexicographically Smallest Equivalent String - https://leetcode.com/problems/lexicographically-smallest-equivalent-string/

# Union Find class
class DSU:
    def __init__(self, size):
        self.parent = {chr(ord("a")+i):chr(ord("a")+i) for i in range(size)}
        
    def find(self, x):
        if self.parent[x] == x: 
            return x
        parent = self.find(self.parent[x])
        self.parent[x] = parent
        return parent
    
    def union(self, x, y):
        rooty = self.find(y)
        rootx = self.find(x)
        if rootx < rooty:
            self.parent[rooty] = rootx
        else:   
            self.parent[rootx] = rooty
                
    def connected(self, x, y):
        return self.find(x) == self.find(y)

class Solution:
    def smallestEquivalentString(self, s1: str, s2: str, baseStr: str) -> str:
        uf = DSU(26)
        for i in range(len(s1)):
            uf.union(s1[i], s2[i])
        res = []
        for a in baseStr:
            res.append(min(a, uf.find(a)))
        return "".join(res)