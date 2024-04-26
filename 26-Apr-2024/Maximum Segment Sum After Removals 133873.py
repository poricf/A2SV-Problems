# Problem: Maximum Segment Sum After Removals - https://leetcode.com/problems/maximum-segment-sum-after-removals/description/

class DSU:
    def __init__(self, n):
        self.rank = [0] * (n + 1)
        self.parent = list(range(n + 1))
        self.size = [1] * (n + 1)
        self.sum = defaultdict(int)
    
    def solve(self,i,num):
        self.sum[i] = num
        
        if i - 1 in self.sum: self.Runion(i - 1, i)
        if i + 1 in self.sum: self.Runion(i + 1, i)
        father = self.find(i)
        return self.sum[father]



    

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
        p_u = self.find(u)
        p_v = self.find(v)
        if p_u == p_v:
            return
        if self.rank[p_u] < self.rank[p_v]:
            self.parent[p_u] = p_v
            self.sum[p_v] += self.sum[p_u]
        elif self.rank[p_v] < self.rank[p_u]:
            self.parent[p_v] = p_u
            self.sum[p_u] += self.sum[p_v]
        else:
            self.parent[p_v] = p_u
            self.rank[p_u] += 1
            self.sum[p_u] += self.sum[p_v]

    def Sunion(self, u, v):
        p_u = self.find(u)
        p_v = self.find(v)
        if p_u == p_v:
            return
        if self.size[p_u] < self.size[p_v]:
            self.parent[p_u] = p_v
            self.size[p_v] += self.size[p_u]
        else:
            self.parent[p_v] = p_u
            self.size[p_u] += self.size[p_v]

class Solution:
    def maximumSegmentSum(self, nums: List[int], removeQueries: List[int]) -> List[int]:
        ans = []
        n = len(nums)
        dsu = DSU(n)
        mx_sm = 0
        for i in reversed(range(n)):
            ans.append(mx_sm)
            q = removeQueries[i]
            mx_sm = max(mx_sm, dsu.solve(q,nums[q]))
        
        return reversed(ans)
