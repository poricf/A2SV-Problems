class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        s, maxx = 0, nums[0]
        for i in nums:
            s += i
            maxx = max(s,maxx)
            if s<0:
                s = 0
        return maxx 