class Solution:
    def numSubseq(self, nums: List[int], target: int) -> int:
        MOD = 10**9 + 7
        left = 0
        right = len(nums) - 1
        nums.sort()
        ans = 0
        while left <= right:
            if nums[right] + nums[left] > target:
                right -= 1
            else:
                n = right - left
                ans += 2 ** n
                left += 1
                # print(ans)
        
        return ans % MOD


        