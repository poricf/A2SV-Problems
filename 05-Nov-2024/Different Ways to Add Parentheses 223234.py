# Problem: Different Ways to Add Parentheses - https://leetcode.com/problems/different-ways-to-add-parentheses/

class Solution:
    def diffWaysToCompute(self, expression: str) -> List[int]:
        @cache
        def dp(lo,hi):
            if lo+1 == hi or lo+2 == hi:
                return [int(expression[lo:hi])]
            ans = []
            for i in range(lo,hi):
                if expression[i] in ['+','-','*']:
                    A = dp(lo,i) 
                    B = dp(i+1,hi)
                    for a in A:
                        for b in B:
                            if expression[i] == '+':
                                ans.append(a+b)
                            elif expression[i] == '-':
                                ans.append(a-b)
                            else:
                                ans.append(a*b)
            return ans
        return dp(0,len(expression))
            


        