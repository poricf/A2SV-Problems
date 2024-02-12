class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        pref_Count = {0:1} 
        res  = 0
        curSum = 0

        for n in nums:
            curSum += n
            diff = curSum - goal
            res += pref_Count.get(diff,0)
            pref_Count[curSum] = 1 + pref_Count.get(curSum,0)

        return res