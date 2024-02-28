class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        l = 0 
        seen = defaultdict(int)
        mx  = 0
        res = 0
        for i,num in enumerate(nums):
            if num in seen:
                while l < seen[num] + 1:
                    mx -= nums[l]
                    l += 1
            seen[num] = i
            mx += num

            res = max(res,mx)
        return res


            
