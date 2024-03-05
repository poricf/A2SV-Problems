class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        n = len(nums)
        subset = []
        def backtrack(i):
            if i >= n:
                res.append(subset[:])
                return
            
            #pick
            subset.append(nums[i])
            backtrack(i + 1)
            subset.pop()
            #dontpick
            backtrack(i + 1)

            
            # backtrack(i + 1,subset)
        
        backtrack(0)

        return res       
        