# Problem: Maximum Width Ramp - https://leetcode.com/problems/maximum-width-ramp

from typing import List

class Solution:
    def maxWidthRamp(self, nums: List[int]) -> int:
        arr = []
        for i in range(len(nums)):
            arr.append((nums[i], i))
        
        arr.sort()
        
        ans = 0
        mini = arr[0][1]
        
        for i in range(1, len(arr)):
            if arr[i][1] > mini:
                ans = max(ans, arr[i][1] - mini)
            mini = min(mini, arr[i][1])
        
        return ans