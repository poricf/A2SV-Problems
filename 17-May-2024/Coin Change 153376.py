# Problem: Coin Change - https://leetcode.com/problems/coin-change/

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        if amount == 0:
            return 0
        @cache
        def dp(idx, _sum):
            if _sum == amount:
                return 0

            if idx >= len(coins) or _sum > amount:
                return float('inf')
            rec1 = dp(idx+1, _sum)
            rec2 = dp(idx, _sum+coins[idx])
            ans = min(rec1, rec2+1)          
            return ans
            


        ans = dp(0, 0)
        if ans == float('inf'):
            return -1

        else:
            return ans
            


            



        