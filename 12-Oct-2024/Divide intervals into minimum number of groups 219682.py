# Problem: Divide intervals into minimum number of groups - https://leetcode.com/problems/divide-intervals-into-minimum-number-of-groups/

class Solution:
    def minGroups(self, intervals: List[List[int]]) -> int:
        pc = defaultdict(int)

  
        for i in intervals:
            pc[i[0]] += 1 
            pc[i[1] + 1] -= 1  

        ci = 0
        max_ci = 0

        for p in sorted(pc.keys()):
            ci += pc[p] 
            max_ci = max(max_ci, ci)  

        return max_ci