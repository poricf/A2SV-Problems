class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = []
        n = len(nums)
        nums.sort()
        def backtrack(i,subset):
            if i >= n:
                res.append(subset[:])
                return
            
            
            #pick
            subset.append(nums[i])
            backtrack(i + 1,subset)
            subset.pop()
            #dontpick
            while i + 1 < n and nums[i+1] == nums[i]:
                i += 1
            backtrack(i + 1,subset)

            
            # backtrack(i + 1,subset)
        
        backtrack(0,[])

        return res  