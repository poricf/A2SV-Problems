# Problem: Maximize Score of Numbers in Ranges - https://leetcode.com/problems/maximize-score-of-numbers-in-ranges/

class Solution:
    def maxPossibleScore(self, start: List[int], d: int) -> int:
        start.sort()
        n = len(start)
        l = 0
        ans=-1
        r = start[-1] - start[0] + d

        def check(score):
            pre = start[0]
            for i in range(1, n):
                if start[i] + d - pre < score:
                    return False
                pre =max(start[i],pre + score)
            return True

        while l <= r:
            m = l + (r - l) // 2
            if check(m):
                ans=m
                l = m + 1
            else:
                r = m-1
        return ans