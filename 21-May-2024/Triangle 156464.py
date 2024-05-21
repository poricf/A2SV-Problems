# Problem: Triangle - https://leetcode.com/problems/triangle/

class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        n = len(triangle)
        m = len(triangle[-1])
        if n == 1:
            return triangle[0][0]
        
        dp = [0] * (m+1)

        for row in triangle[::-1]:
            for i , elem in enumerate(row):
                dp[i] = elem + min(dp[i],dp[i+1])
        
        return dp[0]

