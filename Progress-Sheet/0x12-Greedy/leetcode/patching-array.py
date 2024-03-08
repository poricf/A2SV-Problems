class Solution:
    def minPatches(self, nums: List[int], n: int) -> int:
        _sum = 0
        ans = 0
        i = 0
        while _sum < n:
            if i < len(nums) and nums[i] - 1 <= _sum:
                _sum += nums[i]
                i += 1
            else:
                _sum += _sum+1
                ans += 1
        
        return ans