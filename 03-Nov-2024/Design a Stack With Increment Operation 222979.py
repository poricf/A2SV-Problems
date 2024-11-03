# Problem: Design a Stack With Increment Operation - https://leetcode.com/problems/design-a-stack-with-increment-operation/

class CustomStack:

    def __init__(self, maxSize: int):
        self.maxSize = maxSize
        self.stack = []
        self.inc = []

    def push(self, x: int) -> None:
        if len(self.stack) < self.maxSize:
            self.stack.append(x)
            self.inc.append(0) 

    def pop(self) -> int:
        if not self.stack:
            return -1
        idx = len(self.stack) - 1
        result = self.stack[idx] + self.inc[idx]  
        if idx > 0:
            self.inc[idx - 1] += self.inc[idx] 
        self.stack.pop()
        self.inc.pop()
        return result

    def increment(self, k: int, val: int) -> None:
        limit = min(k, len(self.stack)) - 1
        if limit >= 0:
            self.inc[limit] += val 