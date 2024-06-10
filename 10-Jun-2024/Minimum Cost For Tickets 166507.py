# Problem: Minimum Cost For Tickets - https://leetcode.com/problems/minimum-cost-for-tickets/

class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        @cache
        def dp(day):
            if day <= 0: return 0
            if day not in days: return dp(day-1)
            return min(dp(day-1)+costs[0], dp(day-7)+costs[1], dp(day-30)+costs[2])

        return dp(days[-1])