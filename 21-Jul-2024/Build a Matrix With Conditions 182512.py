# Problem: Build a Matrix With Conditions - https://leetcode.com/problems/build-a-matrix-with-conditions/

class Solution(object):
    def buildMatrix(self, k, rowConditions, colConditions):
        rg = defaultdict(list)
        for u, v in rowConditions:
            rg[u].append(v)       
        cg = defaultdict(list)
        for u, v in colConditions:
            cg[u].append(v)
        def TS(graph):
            indig = {i: 0 for i in range(1, k + 1)}
            for u in graph:
                for v in graph[u]:
                    indig[v] += 1
            q = deque([i for i in indig if indig[i] == 0])
            ordr = []
            while q:
                node = q.popleft()
                ordr.append(node)
                for v in graph[node]:
                    indig[v] -= 1
                    if indig[v] == 0:
                        q.append(v)
            return ordr if len(ordr) == k else []
        rowordr = TS(rg)
        colordr = TS(cg)
        if not rowordr or not colordr:
            return []
        rp = {num: i for i, num in enumerate(rowordr)}
        cp = {num: i for i, num in enumerate(colordr)}
        res = [[0] * k for _ in range(k)]
        for i in range(1, k + 1):
            res[rp[i]][cp[i]] = i
        return res
        