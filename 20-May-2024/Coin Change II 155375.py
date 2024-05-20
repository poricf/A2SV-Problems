# Problem: Coin Change II - https://leetcode.com/problems/coin-change-ii/

class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        N = amount 
        dp = [0] * (N+1)
        dp[0] = 1
        for coin in coins:
            for i in range(coin, N+1):
                dp[i] = (dp[i] +  dp[i - coin])
        
        return dp[N]