# Problem: Target Sum - https://leetcode.com/problems/target-sum/

class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        cache = {}
        def dp(idx, _sum):
            if idx >= len(nums):
                if _sum == target:
                    return 1
                return 0
                
            if (idx, _sum) not in cache:
                cache[(idx, _sum)] = dp(idx+1, _sum+nums[idx]) + dp(idx+1, _sum-nums[idx])
            return cache[(idx, _sum)]

        return dp(0, 0)
            
