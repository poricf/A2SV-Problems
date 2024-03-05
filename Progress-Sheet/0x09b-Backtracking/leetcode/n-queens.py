from typing import List

class Solution:
    def solve(self, col, board, ans, n, leftRow, upperDiag, lowerDiag):
        # base case
        if col == n:
            ans.append([''.join(row) for row in board])
            return

        for row in range(n):
            rowcheck =  leftRow[row] == 0
            uppDiagcheck = upperDiag[row+col] == 0
            lowDiagcheck =  lowerDiag[n-1+(col-row)] == 0
            if rowcheck and uppDiagcheck and lowDiagcheck:
                # hash marking
                leftRow[row] = 1
                upperDiag[row+col] = 1
                lowerDiag[n-1+(col-row)] = 1
                # backtracking
                board[row][col] = 'Q'
                self.solve(col+1, board, ans, n, leftRow, upperDiag, lowerDiag)
                # unmarking
                board[row][col] = '.'
                lowerDiag[n-1+(col-row)] = 0
                upperDiag[row+col] = 0
                leftRow[row] = 0

    def solveNQueens(self, n: int) -> List[List[str]]:
        board = [['.' for _ in range(n)] for _ in range(n)]
        ans = []
        leftRow = [0] * n
        upperDiag = [0] * (2 * n - 1)
        lowerDiag = [0] * (2 * n - 1)

        self.solve(0, board, ans, n, leftRow, upperDiag, lowerDiag)
        return ans