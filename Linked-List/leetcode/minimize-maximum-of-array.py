class Solution:
    def minimizeArrayValue(self, nums: List[int]) -> int:
        ans = 0
        pref = 0
        for i,num in enumerate(nums):
            pref += num
            av = ceil(pref/(i+1))
            ans = max(ans,av)
        return ans
            