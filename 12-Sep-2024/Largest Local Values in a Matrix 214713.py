# Problem: Largest Local Values in a Matrix - https://leetcode.com/problems/largest-local-values-in-a-matrix/

class Solution:
    def largestLocal(self, grid: List[List[int]]) -> List[List[int]]:
   
        n = len(grid)
        result = []
        for i in range (n-2):
            result.append([0]* (n-2))
        #result = [[0]*(n - 2)] *(n-2) - WRONG - it copies reference
        for i in range(n-2):
            for j in range(n-2):
                result[i][j] = max(map(max, ([item [j:j+3] for item in grid[i:i+3]])))
        return result