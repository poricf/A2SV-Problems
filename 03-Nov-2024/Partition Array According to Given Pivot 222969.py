# Problem: Partition Array According to Given Pivot - https://leetcode.com/problems/partition-array-according-to-given-pivot/description/

class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        n=len(nums)
        lis1=[]
        lis2=[]
        lis3=[]
        for i in range(n):
            if pivot < nums[i]:
                lis1.append(nums[i])
            if pivot > nums[i]:
                lis2.append(nums[i])
            if pivot == nums[i]:
                lis3.append(nums[i])
        ans=lis2+lis3+lis1
        return ans