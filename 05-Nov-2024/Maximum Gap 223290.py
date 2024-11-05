# Problem: Maximum Gap - https://leetcode.com/problems/maximum-gap/

class Solution:
    def maximumGap(self, nums):
        if len(nums) < 2:
            return 0
        
        min_n, max_n = min(nums), max(nums)
        
        if min_n == max_n:
            return 0
        
        b_size = max(1, (max_n - min_n) // (len(nums) - 1))
        b_count = (max_n - min_n) // b_size + 1
        
        buckets = [[float('inf'), float('-inf')] for _ in range(b_count)]
        
        for n in nums:
            b_idx = (n - min_n) // b_size
            buckets[b_idx][0] = min(buckets[b_idx][0], n)
            buckets[b_idx][1] = max(buckets[b_idx][1], n)
        
        max_gap = 0
        prev_max = min_n
        
        for b in buckets:
            if b[0] == float('inf'):
                continue
            max_gap = max(max_gap, b[0] - prev_max)
            prev_max = b[1]
        
        return max_gap