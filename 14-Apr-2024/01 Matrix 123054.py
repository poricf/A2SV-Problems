# Problem: 01 Matrix - https://leetcode.com/problems/01-matrix/

class Solution:
    def updateMatrix(self, mat: List[List[int]]):
        n = len(mat)
        m = len(mat[0])
        def inbound(nr , nc):
            return 0<=nr<n  and 0 <= nc < m

        def dfs():
            q = deque()
            for row in range(n):
                for col in range(m):
                    if mat[row][col] == 0:
                        q.append((row, col))
                    else:
                        mat[row][col] = "#"  
            direction = [(1 , 0), (0 , 1), ([-1, 0]), (0 , -1)]
            while q:
                for c in range(len(q)):
                    row, col = q.popleft()
                    for i, j in direction:
                        n_row = row + i
                        n_col = col + j
                        if  inbound (n_row , n_col) and mat[n_row][n_col] == "#":
                            mat[n_row][n_col] = mat[row][col] + 1
                            q.append((n_row, n_col))
        dfs()
        return mat