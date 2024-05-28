# Problem: Palindrome Partitioning - https://leetcode.com/problems/palindrome-partitioning/

class Solution:
    def partition(self, s: str) -> List[List[str]]:
        ans= []
       
        def is_pal(li):
            for l in li:
                if l != l[::-1]:
                    return False
            return True
        

        def backtrack(idx, curr):
            if idx >= len(s):
                if is_pal(curr):
                    ans.append(curr[:])
                return

            for i in range(idx,len(s)):
                curr.append(s[idx:i+1])
                backtrack(i+1, curr)
                curr.pop()
        backtrack(0, [])
        return ans


