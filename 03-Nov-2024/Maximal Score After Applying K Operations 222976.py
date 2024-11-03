# Problem: Maximal Score After Applying K Operations - https://leetcode.com/problems/maximal-score-after-applying-k-operations

class Solution:
    def maxKelements(self, nums: List[int], k: int) -> int:
        

        pq = [-num for num in nums]
        heapq.heapify(pq)  
        score = 0
        while k > 0:
            ele = -heapq.heappop(pq)  
            score += ele
            heapq.heappush(pq, -math.ceil(ele / 3)) 
            k -= 1
        
        return score