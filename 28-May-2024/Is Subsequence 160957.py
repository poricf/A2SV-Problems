# Problem: Is Subsequence - https://leetcode.com/problems/is-subsequence/

class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        @cache
        def dp(idx1, idx2):
            if idx1 >= len(s):
                return True

            if idx2 >= len(t):
                return False

            if s[idx1] == t[idx2]:
                return dp(idx1+1, idx2+1)

            else:
                return dp(idx1, idx2+1)

        return dp(0, 0)

        