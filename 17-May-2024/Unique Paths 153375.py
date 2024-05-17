# Problem: Unique Paths - https://leetcode.com/problems/unique-paths/

class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [[0] * (n + 2) for i in range(m+2)]
        # print(dp)
        

        for i in range(1,m+2):
            for j in range(1,n+2):
                if i == 1 or j == 1:
                    dp[i][j] = 1
                else:
                    dp[i][j] = dp[i-1][j] + dp[i][j-1]
        print(dp)
        return dp[m][n]

        