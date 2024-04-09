# Problem: Check if There is a Valid Path in a Grid - https://leetcode.com/problems/check-if-there-is-a-valid-path-in-a-grid/

class Solution:
    def hasValidPath(self, grid: List[List[int]]) -> bool:
        n = len(grid)
        m = len(grid[0])
        directions = {
        1: [(0,-1),(0,1)],
        2: [(-1,0),(1,0)],
        3: [(0,-1),(1,0)],
        4: [(0,1),(1,0)],
        5: [(0,-1),(-1,0)],
        6: [(0,1),(-1,0)]
       }
               

        Tekebay = {
            (0, 1):[1, 3, 5],
            (0, -1):[1, 4, 6],
            (1, 0):[2, 5, 6],
            (-1, 0):[2, 3, 4]
        }
        def inbound(row, col):
            return 0 <= row < len(grid) and 0 <= col < len(grid[0])

        visited = set()
        q = deque()
        q.append((0,0))
        

        while q:
            row , col = q.popleft()

            if row == n - 1 and col == m - 1:
                return True
            visited.add((row,col))

            for  dr,dc in directions[grid[row][col]]:
                nrow = dr + row
                ncol = dc + col

                if inbound(nrow,ncol) and grid[nrow][ncol] in Tekebay[(dr,dc)] and (nrow,ncol) not in visited:
                    q.append((nrow,ncol))
        
        return False