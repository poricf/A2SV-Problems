# Problem: Maximum Performance of a Team - https://leetcode.com/problems/maximum-performance-of-a-team/

class Solution:
    def maxPerformance(self, n: int, speed: List[int], efficiency: List[int], k: int) -> int:
        heap = []
        tasks = []
        for i in range(n):
            heappush(heap, (-efficiency[i], speed[i]))
        ans = 0
        curr_sum = 0
        idx = 0

        while idx < n:
            if len(tasks) < k:
                task  = heappop(heap)
                heappush(tasks, task[1])
                curr_sum += task[1]
                ans = max(ans, curr_sum * -task[0])
                idx += 1
            else:
                ans = max(ans, curr_sum * -task[0])
                curr_sum -= heappop(tasks)
        return ans % (pow(10, 9) + 7)



