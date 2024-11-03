# Problem: Minimum Deletions to Make String Balanced - https://leetcode.com/problems/minimum-deletions-to-make-string-balanced/

class Solution:
    def minimumDeletions(self, s: str) -> int:
        count = Counter(s)
        ans = 0
        cnt = 0
        for c in s:
            if c == 'b':
                cnt += 1
            else:
                ans = min(ans + 1 , cnt)

        
        return ans

