# Problem: Car fleet - https://leetcode.com/problems/car-fleet/

class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        n = len(speed)
        time = []
        new_arr = [(position[i],speed[i],i) for i in range(n)]
        new_arr.sort()
        for x,v,i in new_arr:
            t = (target - x)/v
            time.append(t)

        stack = []
        for t in time:
            while stack and t >= stack[-1]:
                stack.pop()
            stack.append(t)
       
        return len(stack)