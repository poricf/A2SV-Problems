class Solution:
    def canJump(self, nums: List[int]) -> bool:
        MaxICanReach = 0
        
        for i in range(len(nums)):
            if i > MaxICanReach:
                return False
            MaxICanReach = max(MaxICanReach, i+nums[i])
        
        return True
            
        
        

