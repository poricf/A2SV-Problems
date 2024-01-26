class Solution:
    def findMiddleIndex(self, nums: List[int]) -> int:
        n = len(nums)
        pref = [0]*(n+1)
        comp = sum(nums)
        for i in range(1,n+1):
            pref[i] = pref[i-1] + nums[i-1]
        # print(pref)
        for i in range(n):
            comp -= nums[i]
            if comp == pref[i]:
                return i
            
        return -1