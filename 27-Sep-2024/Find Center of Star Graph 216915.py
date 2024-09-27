# Problem: Find Center of Star Graph - https://leetcode.com/problems/find-center-of-star-graph/

class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        N = len(edges)
        edgecount = [0] * (N + 1)
        for edge in edges:
            u , v = edge
            edgecount[u-1] += 1
            edgecount[v-1] += 1
        
        ans = edgecount.index((max(edgecount)))

        return ans + 1
