# Problem: Shortest Path in Binary Matrix - https://leetcode.com/problems/shortest-path-in-binary-matrix/description/

class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        def inbound(row, col):
            return (0 <= row < len(grid) and 0 <= col < len(grid[0]))
        '''
        0,1,0,0,0
        0,1,0,1,0
        0,1,1,1,0
        0,1,0,1,0
        0,0,1,1,0
        '''
        directions = [[1, 1], [1, 0], [0, 1], [-1, 1], [1, -1], [-1, 0], [0, -1], [-1, -1]]
        
        n = len(grid)
        sr , sc = 0 , 0
        dr , dc = n - 1, n - 1
        ##################################
        if grid[sr][sc] != 0:
            return -1
        ###################################
        length = 0
        q = deque()
        q.append([sr,sc,length])
        visited = set((0,0))
        
        while q:
            row , col , length = q.popleft()

            if row == dr and col == dc:
                return length + 1


            for r,c in directions:
                nrow = r + row
                ncol = c + col

                if inbound(nrow,ncol) and grid[nrow][ncol] == 0 and (nrow,ncol) not in visited:
                    visited.add((nrow,ncol))
                    q.append([nrow,ncol,length + 1])

        return -1