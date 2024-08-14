# Problem: Magnetic Force Between Two Balls - https://leetcode.com/problems/magnetic-force-between-two-balls/

class Solution:
    def maxDistance(self, position: List[int], m: int) -> int:


        position.sort()
        n = len(position)

        def check(mid):
            balls = 1
            prev = position[0]
            for i in range(1,n):
                if position[i] - prev >= mid:
                    balls += 1
                    prev = position[i]
            return balls >= m

        
        low = 1
        high =  10 ** 10
        while low <= high:
            mid=(low+high)//2
            if check(mid):
                low=mid+1
                best = mid
            else:
                high=mid-1
        return best                      