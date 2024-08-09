# Problem: Daily Temperatures - https://leetcode.com/problems/daily-temperatures/

class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        answer = [0] * (len(temperatures))

        indexed_temp = [(i,temp) for i,temp in enumerate(temperatures) ]
        
        stack = []

        for ind,temp in indexed_temp:
            while stack and stack[-1][1] < temp:
                i,t = stack.pop()
                answer[i] = ind - i
            stack.append((ind,temp))
        return answer