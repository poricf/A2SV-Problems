# Problem: Letter Case Permutation - https://leetcode.com/problems/letter-case-permutation/

class Solution:
    def letterCasePermutation(self, S):
        ans = []
        def backtrack(s, i, ans):
            if i == len(s):
                ans.append(''.join(s))
                return
            
            c = s[i]
            s[i] = c.upper() if c.islower() else c.lower()
            backtrack(s, i + 1, ans)
            
            if c.isalpha():
                s[i] = c
                backtrack(s, i + 1, ans)
        
        
        backtrack(list(S), 0, ans)
        return ans
    