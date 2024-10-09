# Problem: Minimum Add To Make Parentheses Valid - https://leetcode.com/problems/minimum-add-to-make-parentheses-valid/

class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        stack=[]
        for i in s:
            if len(stack)==0:
                stack.append(i)
            elif i==')' and stack[-1]=='(':
                stack.pop()
            else:
                stack.append(i)



                
        return len(stack)