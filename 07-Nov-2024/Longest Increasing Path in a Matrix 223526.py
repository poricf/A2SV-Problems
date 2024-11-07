# Problem: Longest Increasing Path in a Matrix - https://leetcode.com/problems/longest-increasing-path-in-a-matrix/

class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:

        n = len(matrix)
        m = len(matrix[0])

        LIP = [[0] * m for i in range(n)]

        dirx = [(0, 1), (1, 0), (0, -1), (-1, 0)]

        def inbound(i, j):
            return 0 <= i < n and 0 <= j < m

        def dfs(i, j):
            if LIP[i][j] != 0:
                return LIP[i][j]
            
            max_len = 1
            for x, y in dirx:
                nx = i + x
                ny = j + y
                
                if inbound(nx, ny) and matrix[nx][ny] > matrix[i][j]:
                    max_len = max(max_len, 1 + dfs(nx, ny))
            
            LIP[i][j] = max_len
            return LIP[i][j]

        for i in range(n):
            for j in range(m):
                if LIP[i][j] == 0:
                    dfs(i, j)
    
        mx = 1
        for row in LIP:
            mx = max(mx, max(row))
        
        return mx



