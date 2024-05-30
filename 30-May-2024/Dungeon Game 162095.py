# Problem: Dungeon Game - https://leetcode.com/problems/dungeon-game/

class Solution:
    def calculateMinimumHP(self, dungeon: List[List[int]]) -> int:
        n, m = len(dungeon), len(dungeon[0]) 
        dp = [[-inf for _ in range(m + 1)] for _ in range(n + 1)]
        dp[n - 1][m - 1] = dungeon[n - 1][m - 1]

        for i in range(n - 1, -1, -1):
            for j in range(m - 1, -1, -1):
                if (i, j) == (n - 1, m - 1):
                    continue
                
                down = min(dungeon[i][j] + dp[i][j + 1], dungeon[i][j])
                right = min(dungeon[i][j] + dp[i + 1][j], dungeon[i][j])

                dp[i][j] = max(down, right)
        
        return max(1, -dp[0][0] + 1)
