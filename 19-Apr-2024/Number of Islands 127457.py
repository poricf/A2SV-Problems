# Problem: Number of Islands - https://leetcode.com/problems/number-of-islands/

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        def inbound(row, col):
            return (0 <= row < len(grid) and 0 <= col < len(grid[0]))
        
        n = len(grid)
        m = len(grid[0])

        ans = 0

        vis = set()

        def dfs(row,col):
            vis.add((row,col))

            dir = [[0,1], [0,-1], [1,0], [-1,0]]

            for dr,dc in dir:
                nrow = row + dr
                ncol = col + dc

                if inbound(nrow,ncol) and (nrow,ncol) not in vis and grid[row][col] == '1':
                    dfs(nrow,ncol)


        for row in range(n):
            for col in range(m):
                if grid[row][col] == '1' and (row,col) not in vis :
                    ans += 1
                    dfs(row,col)
        
        return ans