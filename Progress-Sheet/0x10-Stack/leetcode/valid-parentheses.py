class Solution:
    def isValid(self, s: str) -> bool:
        '''
        create stack - then while iterating through it if u got opening then push closing bracket 
        ([])

        stack = }]

        when getting closing bracket then it shoud be the same as the stack top

        '''
        if len(s) < 2:
            return False
        stack = []

        for c in s:
            if c == '(':
                stack.append(')')
            elif c == '[':
                stack.append(']')
            elif c == '{':
                stack.append('}')
            else:

                if len(stack) == 0 or stack.pop() != c:
                    return False

        return len(stack) == 0
            