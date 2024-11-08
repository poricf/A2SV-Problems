# Problem: Minimum Difference Between Largest and Smallest Value in 3 Moves - https://leetcode.com/problems/minimum-difference-between-largest-and-smallest-value-in-three-moves/

class Solution:
    def minDifference(self, nums: List[int]) -> int:
        nums.sort()
        
        if len(nums) < 5:
            return 0
        dif1 = nums[-1] - nums[3]
        dif2 =  nums[-2] - nums[2]
        dif3 =  nums[-3] - nums[1]
        dif4 = nums[-4] - nums[0]

        return min(dif1, dif2 , dif3 , dif4)