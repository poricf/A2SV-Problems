# Problem: Minimum Score of a Path Between Two Cities - https://leetcode.com/problems/minimum-score-of-a-path-between-two-cities/description/

class Solution:
    def find(self, node, dictu):
        if node not in dictu:
            dictu[node] = [node, 1]
        elif dictu[node][0] != node:
            dictu[node][0] = self.find(dictu[node][0], dictu)
        return dictu[node][0]

    def minScore(self, n: int, roads: List[List[int]]) -> int:
        dictu = defaultdict(int)
        for i in roads:
            p1 = self.find(i[0], dictu)
            p2 = self.find(i[1], dictu)
            if p1 != p2:
                if dictu[p1][1] >= dictu[p2][1]:
                    dictu[p2][0] = p1
                    dictu[i[0]][0] = p1
                    dictu[i[1]][0] = p1
                    dictu[p1][1] += dictu[p2][1]
                else:
                    dictu[p1][0] = p2
                    dictu[i[0]][0] = p2
                    dictu[i[1]][0] = p2
                    dictu[p2][1] += dictu[p1][1]
        result_parent = self.find(dictu[1][0], dictu)
        mini = sys.maxsize
        for i in roads:
            p1 = self.find(i[0], dictu)
            p2 = self.find(i[1], dictu)
            if p1 == result_parent or p2 == result_parent:
                mini = min(mini, i[-1])
        return mini