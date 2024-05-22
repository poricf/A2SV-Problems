# Problem: Unique Paths II - https://leetcode.com/problems/unique-paths-ii/

class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        rows, cols = len(obstacleGrid), len(obstacleGrid[0])
        dp = [[0] * cols for _ in range(rows)]

        if obstacleGrid[0][0] == 0:
            dp[0][0] = 1
      
   
        for i in range(1, rows):
            if obstacleGrid[i][0] == 0:  
                dp[i][0] = dp[i-1][0]  
      
       
        for j in range(1, cols):
            if obstacleGrid[0][j] == 0:  
                dp[0][j] = dp[0][j-1]  

      
        for i in range(1, rows):
            for j in range(1, cols):
                if obstacleGrid[i][j] == 0:  
                    dp[i][j] = dp[i-1][j] + dp[i][j-1] 
      
        return dp[-1][-1]