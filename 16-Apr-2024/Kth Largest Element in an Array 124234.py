# Problem: Kth Largest Element in an Array - https://leetcode.com/problems/kth-largest-element-in-an-array/description/

import heapq
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heapq.heapify(nums)
        
        largest = heapq.nlargest(k,nums)
        
        return largest[-1]
