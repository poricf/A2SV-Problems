# Problem: Find the Town Judge - https://leetcode.com/problems/find-the-town-judge/

class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        if n == 1:
            return 1

        edges_in = defaultdict(int)
        edges_out = defaultdict(int)

        for i, j in trust:
            edges_in[j] += 1
            edges_out[i] += 1

        for i, v in edges_in.items():
            if v == n - 1 and edges_out[i] == 0:
                return i

        return -1
        

      