# Problem: Best Time to Buy and Sell Stock with Cooldown - https://leetcode.com/problems/best-time-to-buy-and-sell-stock-with-cooldown/

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        @cache
        def dp(idx, state):
            if idx >= len(prices):
                return 0

            if state == 0:
                b = dp(idx+1, 1) - prices[idx]
                nb = dp(idx+1, 0)
                return max (b, nb)
            elif state == 1:
                s = dp(idx+1, -1) + prices[idx]
                ns = dp(idx+1, 1)
                return max (s, ns)

            else:
                c = dp(idx+1, 0)
                nc = dp(idx+1, -1)
                return max(c, nc)
        return dp(0,0)



        