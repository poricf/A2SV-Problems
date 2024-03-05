class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        for char in s:
            if char == ']':
                text = []
                number = []
                while stack[-1] != '[':
                    text.append(stack.pop())
                stack.pop()
                while stack and stack[-1].isdigit():
                    number.append(stack.pop())
                number = int("".join(number[::-1]))
                text = "".join(text[::-1])
                stack.append(number*text)
            else:
                stack.append(char)
        return "".join(stack)