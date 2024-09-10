# Problem: Maximum Distance in Arrays - https://leetcode.com/problems/maximum-distance-in-arrays/

class Solution:
    def maxDistance(self, arrays: List[List[int]]) -> int:
        n = len(arrays)
        arrays.sort()
        mn = arrays[0][0]
        mx = float("-inf")
        for i in range(1,n):
            nums = arrays[i]
            mx = max(mx,max(nums))
        
        pos = abs(mx - mn)
        for i in range(n):
            nums = arrays[i]
            mxnums = nums[len(nums) - 1]
            if mxnums >= mx:
                mx = mxnums
                ans = i
        mn = float("inf")
        for i in range(n):
            if i == ans:
                continue
            nums = arrays[i]
            mn = min(nums[0],mn)

        
        pos2 = abs(mx - mn)

        return max(pos,pos2)
        
        
        

