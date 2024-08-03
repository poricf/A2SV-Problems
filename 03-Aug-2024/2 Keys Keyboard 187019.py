# Problem: 2 Keys Keyboard - https://leetcode.com/problems/2-keys-keyboard/description/

class Solution:
    def minSteps(self, n: int) -> int:
        dp = [float('inf')] * (n + 1)

        dp[0] = dp[1] = 0

        for i in range(2,n + 1):
            dp[i] = min(i,dp[i])
            for j in range(i,n+1,i):
                if j % i == 0:
                    dp[j] = min(dp[j],dp[i] + ( j // i))
        
        print(dp)
                    
      
        return dp[n]