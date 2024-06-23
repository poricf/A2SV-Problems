# Problem: Find Pivot Index - https://leetcode.com/problems/find-pivot-index/

# Time Complexity : O(n)
# Space Complexity : O(1)
class Solution(object):
    def pivotIndex(self, nums):
        leftSum, rightSum = 0, sum(nums)
        for idx, ele in enumerate(nums):
            rightSum -= ele
            if leftSum == rightSum:
                return idx      
            leftSum += ele
        return -1