# Problem: Combination Sum IV - https://leetcode.com/problems/combination-sum-iv/description/

class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        dp = [0 for i in range(target + 1)]
        dp[0] = 1

        for i in range(len(dp)):
            ans = 0
            for num in nums:
                if i - num >= 0:
                    dp[i] += dp[i - num]
            
        
        return dp[target]
                
