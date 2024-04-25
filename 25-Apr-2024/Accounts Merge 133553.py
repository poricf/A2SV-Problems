# Problem: Accounts Merge - https://leetcode.com/problems/accounts-merge/

class DSU:
    def __init__(self, n):
        self.rank = [0] * (n + 1)
        self.parent = list(range(n + 1))
        self.size = [1] * (n + 1)

    def find(self, node):
        if node == self.parent[node]:
            return node

        stack = []
        while node != self.parent[node]:
            stack.append(node)
            node = self.parent[node]

        # Path compression
        for n in stack:
            self.parent[n] = node

        return node

    def Runion(self, u, v):
        rep_u = self.find(u)
        rep_v = self.find(v)
        if rep_u == rep_v:
            return
        if self.rank[rep_u] < self.rank[rep_v]:
            self.parent[rep_u] = rep_v
        elif self.rank[rep_v] < self.rank[rep_u]:
            self.parent[rep_v] = rep_u
        else:
            self.parent[rep_v] = rep_u
            self.rank[rep_u] += 1

    def Sunion(self, u, v):
        rep_u = self.find(u)
        rep_v = self.find(v)
        if rep_u == rep_v:
            return
        if self.size[rep_u] < self.size[rep_v]:
            self.parent[rep_u] = rep_v
            self.size[rep_v] += self.size[rep_u]
        else:
            self.parent[rep_v] = rep_u
            self.size[rep_u] += self.size[rep_v]

class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        n = len(accounts)
        dsu = DSU(n)
        accounts.sort()
        mail_node = defaultdict(int)

        for i in range(n):
            for j in range(1,len(accounts[i])):
                mail = accounts[i][j]
                if mail not in mail_node:
                    mail_node[mail] = i 
                else:
                    dsu.Runion(i,mail_node[mail])
        
        merged = [[] for i in range(n)]

        for mail,node in mail_node.items():
            rep = dsu.find(node)
            merged[rep].append(mail)
        
        ans = []

        for i in range(n):
            if not merged[i]:
                continue
            merged[i].sort()
            temp = [accounts[i][0]] + merged[i]
            ans.append(temp)
        return ans