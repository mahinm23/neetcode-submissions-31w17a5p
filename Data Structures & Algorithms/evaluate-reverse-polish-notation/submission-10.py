class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        result = 0
        for item in tokens:
            if item == '+':
                result = stack[-2] + stack[-1]
                stack.pop()
                stack.pop()
                stack.append(result)
                print(result)
            elif item == '-':
                result = stack[-2] - stack[-1]
                stack.pop()
                stack.pop()
                stack.append(result)
                print(result)
            elif item == '*':
                result = stack[-2] * stack[-1]
                stack.pop()
                stack.pop()
                stack.append(result)
                print(result)
            elif item == '/':
                result = int(stack[-2]/stack[-1])
                stack.pop()
                stack.pop()
                stack.append(result)
                print(result)
            else:
                stack.append(int(item))
            

        return stack[0]