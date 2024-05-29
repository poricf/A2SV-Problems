# Problem: Partition to K Equal Sum Subsets - https://leetcode.com/problems/partition-to-k-equal-sum-subsets/

class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        if len(nums)<k or sum(nums)/k != int(sum(nums)/k): return False
        N = len(nums)
        
        @cache 
        def dp(mask, cur):
            if mask == 0: return cur == 0
            elif cur == 0: return dp(mask, sum(nums)/k)
            for bit in range(len(nums)):
                if mask & (1 << bit):
                    if nums[bit] <= cur and dp(mask ^ (1 << bit), cur-nums[bit]):
                        return True
            return False
    
        return dp(2**N-1, sum(nums)/k)