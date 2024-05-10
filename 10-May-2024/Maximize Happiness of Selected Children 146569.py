# Problem: Maximize Happiness of Selected Children - https://leetcode.com/problems/maximize-happiness-of-selected-children/?envType=daily-question&envId=2024-05-09

class Solution:
    def maximumHappinessSum(self, happiness: List[int], k: int) -> int:
        heap = []
        for val in happiness:
            heappush(heap,-val)
        sub = 0
        sm = 0
        for i in range(k):
            now = -heappop(heap)
            now -= sub
            if now < 0:
                now = 0
           
            
            sm += now
            sub += 1
        return sm

