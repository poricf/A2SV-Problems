# Problem: Minimum Falling Path Sum - https://leetcode.com/problems/minimum-falling-path-sum/

INF = float('inf')
class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        h = len(matrix)
        if h == 0:
            return 0
        w = len(matrix[0])

        dp = [[INF] * w for _ in range(h)]
        dp[-1] = matrix[-1]

        for i in range(h - 2, -1, -1):
            for j in range(w):
                dp[i][j] = matrix[i][j] + min(
                    dp[i + 1][j],  # Directly below
                    dp[i + 1][j - 1] if j > 0 else INF,  #dl
                    dp[i + 1][j + 1] if j < w - 1 else INF #dr
                )

   
        return min(dp[0])