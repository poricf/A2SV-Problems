# Problem: Find the Student that Will Replace the Chalk - https://leetcode.com/problems/find-the-student-that-will-replace-the-chalk/description/

class Solution:
    def chalkReplacer(self, chalk: List[int], k: int) -> int:
        total_chalk = sum(chalk)
        remaining_chalk = k % total_chalk
        
        for i, usage in enumerate(chalk):
            if remaining_chalk < usage:
                return i
            remaining_chalk -= usage