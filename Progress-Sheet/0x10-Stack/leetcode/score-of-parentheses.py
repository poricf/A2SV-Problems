class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        stack = [0]  # Initialize the stack with a base score of 0

        for char in s:
            if char == '(':
                stack.append(0)  # Start a new level of parentheses
            else:
                score = stack.pop()  # Get the score of the current level

                if score == 0:
                    # If the score is 0, it means we have "()"
                    # Increase the score at the previous level by 1
                    stack[-1] += 1
                else:
                    # If the score is not 0, it means we have "(A)"
                    # Double the score at the previous level and add it to the current level
                    stack[-1] += 2 * score

        return stack[0]  # The final score is stored at the base level of the stack