# Problem: Maximal Square - https://leetcode.com/problems/maximal-square/

class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        dp = [[0 for i in range(len(matrix[0]))] for _ in range(len(matrix))]
        max_ = 0

        def inbound(row, col):
            return 0 <= row < len(matrix) and 0 <= col < len(matrix[0])
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == '0':
                    dp[i][j] = 0
                else:
                    up = 0 if not inbound(i-1, j) else matrix[i-1][j]
                    diagonal = 0 if not inbound(i-1, j-1) else matrix[i-1][j-1]
                    left = 0 if not inbound(i, j-1) else matrix[i][j-1]

                    if up == diagonal == left != 0 :
                        dp[i][j] = min(dp[i-1][j-1], dp[i-1][j], dp[i][j-1]) + 1
                    else:
                        dp[i][j] = int(matrix[i][j])
                max_ = max(max_ , dp[i][j])
        
        return max_ * max_


