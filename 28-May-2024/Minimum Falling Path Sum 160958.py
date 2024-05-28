# Problem: Minimum Falling Path Sum - https://leetcode.com/problems/minimum-falling-path-sum/

class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        def inbound(row, col):
            return  0 <= col < len(matrix[0])
        @cache
        def dp(row, col):
            if row >= len(matrix):
                return 0
            left, down, right = float('inf'), float('inf') ,float('inf')
            if inbound(row + 1, col - 1):
                left = matrix[row][col] + dp(row + 1, col - 1)
            
            if inbound(row + 1, col):
                down = matrix[row][col] + dp(row + 1, col)

            if inbound(row + 1, col + 1):
                right = matrix[row][col] + dp(row + 1, col + 1)

            return min(left, down, right)
        ans = float('inf')

        for i in range(len(matrix[0])):
            ans = min(ans , dp(0,i))
        return ans
            


        
        