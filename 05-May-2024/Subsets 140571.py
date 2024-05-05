# Problem: Subsets - https://leetcode.com/problems/subsets/

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        def checkset(x,i):
            if (1 << i) & x:
                return True
            return False
        res = []
        n = len(nums)
        subset = 1 << n

        for num in range(subset):
            temp = []
            for i in range(n):
                
                if checkset(num,i):
                    temp.append(nums[i])
            res.append(temp)
        
        return res

