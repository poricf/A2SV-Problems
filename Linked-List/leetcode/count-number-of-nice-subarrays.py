class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        for i in range(len(nums)):
            nums[i] = 1 if nums[i] % 2 else 0
    
        pref_Count = {0:1} 
        res  = 0
        curSum = 0

        for n in nums:
            curSum += n
            diff = curSum - k
            res += pref_Count.get(diff,0)
            pref_Count[curSum] = 1 + pref_Count.get(curSum,0)

        return res