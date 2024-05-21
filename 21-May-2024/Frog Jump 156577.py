# Problem: Frog Jump - https://leetcode.com/problems/frog-jump/

class Solution:
    def canCross(self, stones: List[int]) -> bool:
        dp = {stone : set() for stone in stones}
        dp[0] = {0}

        for stone in stones:
            for j in dp[stone]:
                for jump in [j + 1, j - 1, j]:
                    if jump <= 0:
                        continue
                    if (stone + jump) in dp:
                        dp[stone + jump].add(jump)
        
        return len(dp[stones[-1]]) >= 1