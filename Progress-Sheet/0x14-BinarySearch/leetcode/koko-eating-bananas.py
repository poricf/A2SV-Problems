class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left, right = 1, max(piles)

        best = max(piles)

        while left <= right:
            mid = (left + right)//2
            calculated_hour = 0
            for i in range(len(piles)):
                calculated_hour += math.ceil(piles[i]/mid)
            
            if calculated_hour > h:
                left = mid + 1
            else:
                best = min(best, mid)
                right = mid - 1

        return best