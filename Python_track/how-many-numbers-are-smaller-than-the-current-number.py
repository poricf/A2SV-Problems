class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        i , j = 0 , 1
        n = len(nums)
        res = []
        for i in range(n):
            ans = 0
            j = 0
            while(j  < n):
                if nums[j] < nums[i]:
                    ans += 1
                j+=1
            res.append(ans)
        return res