# Problem: Find Players With Zero or One Losses - https://leetcode.com/problems/find-players-with-zero-or-one-losses

class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        wincount = defaultdict(int)
        losecount = defaultdict(int)

        for win, lose in matches:
            wincount[win] += 1
            losecount[lose] += 1
        winners = []
        one_losers = []
        for p in wincount:
            if not p in losecount:
                winners.append(p)
        for p in losecount:
            if losecount[p] == 1:
                one_losers.append(p)
        winners.sort()
        one_losers.sort()      
        return [winners, one_losers]