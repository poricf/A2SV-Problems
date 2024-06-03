# Problem: 3Sum - https://leetcode.com/problems/3sum/description/

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        ans = set()
        nums.sort()
        n= len(nums)
        for i in range(n-2):
            j = i+1 
            k = n - 1
            while(j < k):
                remp = nums[i] + nums[j] + nums[k]

                if remp == 0:
                    ans.add((nums[i],nums[j], nums[k]))
                    j += 1
                elif remp > 0:
                    k -= 1
                else:
                    j += 1
        return ans