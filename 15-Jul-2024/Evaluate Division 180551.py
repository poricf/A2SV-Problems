# Problem: Evaluate Division - https://leetcode.com/problems/evaluate-division/

class Disjointset :

    def __init__(self,n):
        self.rank = [0 for i in range(n+1)]   # n+1 because of 0 or 1 based indexing
        self.parent = [i for i in range(n+1)]
        self.size = [1 for i in range(n+1)]

    def findparent(self,node) :
        if node == self.parent[node] :
            return node 
        self.parent[node] = self.findparent(self.parent[node]) 
        return self.parent[node]

    # union by rank
    def unionbyrank(self, u , v) :
        uutp = self.findparent(u)
        vutp = self.findparent(v)
        if uutp == vutp :
            return 
        urank = self.rank[u]
        vrank = self.rank[v]
        if urank < vrank :
            self.parent[uutp] = vutp
        elif urank > vrank :
            self.parent[vutp] = uutp
        else :
            self.parent[vutp] = uutp
            self.rank[uutp] += 1

    # union by size
    def unionbysize(self,u,v) :
        uutp = self.findparent(u)
        vutp = self.findparent(v)
        if uutp == vutp :
            return 

        # finding size
        usize = self.size[uutp]
        vsize = self.size[vutp]
        if usize < vsize :
            self.parent[uutp] = vutp
            self.size[vutp] += self.size[uutp]
        else:
            self.parent[vutp] = uutp 
            self.size[uutp] += self.size[vutp]


class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:

        l = []
        for x in equations :
            l += x
        s = list(set(l))
        s.sort()
        d = {s[i]:i for i in range(len(s))}

        adj = { i :[] for i in range(len(s))}

        obj = Disjointset(len(s))


        for i in range(len(equations)) :
            u = d[equations[i][0]]
            v = d[equations[i][1]]
            cost = values[i]
            adj[u] += [[v,cost]]
            adj[v] += [[u , 1/cost]]
            obj.unionbyrank(u,v)

        # print(adj)


        def dfs(node , end):
            if node == end :
                return 1
            visi[node] = 1
            val = 0
            for x in adj[node] :
                if visi[x[0]] == -1 :
                    val = max( val , x[1] * dfs(x[0],end))
            return val

        ans = []
        for x in queries :
            if x[0] in s and x[1] in s and obj.findparent(d[x[0]]) == obj.findparent(d[x[1]]):
                visi = [-1 for i in range(len(s))]
                a = dfs(d[x[0]] , d[x[1]])
                ans += [a]
            else :
                ans += [-1]
        # print(ans)

        return ans