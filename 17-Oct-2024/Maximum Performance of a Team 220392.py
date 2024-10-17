# Problem: Maximum Performance of a Team - https://leetcode.com/problems/maximum-performance-of-a-team/

class Solution:
    def maxPerformance(self, n: int, speed: List[int], efficiency: List[int], k: int) -> int:
        mod = 10 ** 9 + 7
        nums = []
        for i in range(n):
            t, b = speed[i] , efficiency[i]
            nums.append([t,b])

        nums.sort(reverse = True, key= lambda x: x[1])

        heap = [] 
        ans = 0
        total = 0

        for i in range(n):
            speed, eff = nums[i]
            total += speed

        
            if len(heap) < k:
                heappush(heap,(speed,eff))

            else: 
                min_speed, min_eff = heappop(heap)
                heappush(heap,(speed,eff))
                total -= min_speed

            ans = max(ans,total*eff) 
            
        return ans % mod












