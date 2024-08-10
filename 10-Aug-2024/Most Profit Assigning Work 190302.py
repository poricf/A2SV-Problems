# Problem: Most Profit Assigning Work - https://leetcode.com/problems/most-profit-assigning-work/

class Solution:
    def maxProfitAssignment(self, difficulty: List[int], profit: List[int], worker: List[int]) -> int:
        comb = list(zip(difficulty, profit))
        comb.sort()
        worker.sort()
        cur_max = pointer = answer = 0
        for ablity in worker:
            while pointer <  len(comb) and comb[pointer][0] <= ablity:
                cur_max = max(cur_max, comb[pointer][1])
                pointer += 1
            answer += cur_max
        return answer