# Problem: Max Area of Island - https://leetcode.com/problems/max-area-of-island/

class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        rows,cols = len(grid),len(grid[0])
        visited = [[False for j in range(cols)] for i in range(rows)]
        def dfs(i,j):
            if i<0 or i>= rows or j<0 or j>= cols or grid[i][j]==0 or visited[i][j]:
                return 0
            visited[i][j] = True
            count = 1
            count += dfs(i+1,j)
            count += dfs(i-1,j)
            count += dfs(i,j+1)
            count += dfs(i,j-1)
            return count

        ans = 0
        for i in range(rows):
            for j in range(cols):
                if grid[i][j]==1:
                    count = dfs(i,j)
                    ans = max(count,ans)
        return ans