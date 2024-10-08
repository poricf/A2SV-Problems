# Problem: Set Matrix Zeroes - https://leetcode.com/problems/set-matrix-zeroes/

class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        rLen = len(matrix)
        cLen = len(matrix[0])
        rows = [False] * rLen
        cols = [False] * cLen
        for r in range(rLen):
            for c in range(cLen): 
                if matrix[r][c] == 0:
                    rows[r] = True
                    cols[c] = True
        for i, r in enumerate(rows): 
            if r:
                for c in range(cLen):
                    matrix[i][c] = 0
        for j, c in enumerate(cols):  
            if c:
                for r in range(rLen):
                    matrix[r][j] = 0


        