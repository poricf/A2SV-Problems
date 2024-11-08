# Problem: Minimum Obstacle Removal to Reach Corner - https://leetcode.com/problems/minimum-obstacle-removal-to-reach-corner/

class Solution:
    def minimumObstacles(self, grid: List[List[int]]) -> int:
        n, m = len(grid), len(grid[0])

        visited = [[False]*m for _ in range(n)]
        visited[0][0] = True
        
        obstacles = collections.deque()
        cells_to_move = collections.deque()
        if grid[0][0] == 1:
            obstacles.append((0, 0))
        else:
            cells_to_move.append((0, 0))
        removed = 0
        directions = [(1,0), (0, 1), (-1, 0), (0, -1)]

        def FS(y, x):
            for d_y, d_x in directions:
                    new_y = y + d_y
                    new_x = x + d_x
                    if not (0 <= new_y <n and 0 <= new_x < m):
                        continue
                    if visited[new_y][new_x]:
                        continue
                    
                    visited[new_y][new_x] = True

                    if grid[new_y][new_x] == 1:
                        obstacles.append((new_y,new_x))
                    else:
                        cells_to_move.append((new_y,new_x))
        
        while True:
            while cells_to_move:
                y, x = cells_to_move.popleft()
                if y == n-1 and x == m-1:
                    return removed
                FS(y, x)

            removed += 1

            for _ in range(len(obstacles)):
                y, x = obstacles.popleft()
                FS(y,x)