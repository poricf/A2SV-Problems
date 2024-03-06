from typing import List

class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        def check(mid, weights, days):
            total = 0
            shipments = 1
            for weight in weights:
                total += weight
                if total > mid:
                    shipments += 1
                    total = weight
                    if shipments > days:
                        return False
            return True
        
        left = max(weights)
        right = sum(weights)
        
        while left < right:
            mid = (left + right) >> 1
            if check(mid, weights, days):
                right = mid
            else:
                left = mid + 1
            
        return left