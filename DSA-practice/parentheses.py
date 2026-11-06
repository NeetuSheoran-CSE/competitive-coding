
# 20. Valid Parentheses

class Solution:
    def isValid(self, s: str) -> bool:
        stack=[]
        pairs = {')': '(', ']': '[', '}': '{'}
        for bracket in s:
            if bracket in "({[":
                stack.append(bracket)
            else:
                if not stack:
                    return False
                lastOpen = stack.pop()
                if lastOpen != pairs[bracket]:
                    return False
        return len(stack) == 0
    
    

# Postfix Evaluation

class Solution:
    def evaluatePostfix(self, arr):
        stack = []
        operators = {"+", "-", "*", "/", "^"}

        for token in arr:
            if token not in operators:
                stack.append(int(token))
                continue

            right = stack.pop()
            left = stack.pop()

            if token == "+":
                value = left + right
            elif token == "-":
                value = left - right
            elif token == "*":
                value = left * right
            elif token == "/":
                value = left // right
            else:
                value = int(left ** right)

            stack.append(value)

        return stack[0]