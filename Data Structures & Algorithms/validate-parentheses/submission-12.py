class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        top = -1

        for item in s:
            stack.append(item)
            top += 1
            print(stack)

            if item == ')' and stack[top-1] == '(':
                stack.pop(top)
                stack.pop(top-1)
                top -= 2
            elif item == ']' and stack[top-1] == '[':
                stack.pop(top)
                stack.pop(top-1)
                top -= 2
            elif item == '}' and stack[top-1] == '{':
                stack.pop(top)
                stack.pop(top-1)
                top -= 2

        print(top)
        if top == -1:
            return True
        else: 
            return False