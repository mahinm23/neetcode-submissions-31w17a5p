class Stack:
    
    def __init__(self):
        self.end = -1
        self.stack = []

    def push(self, value) -> None:
        self.stack.append(value)
        self.end += 1

    def pop(self) -> None:
        self.stack.pop()
        self.end -= 1

    def top(self) -> int:
        return self.stack[self.end]


class MinStack:

    def __init__(self):
        self.end = -1
        self.min_stack = Stack()
        self.stack = Stack()

    def push(self, value: int) -> None:
        if self.end == -1:
            self.min_stack.push(value)
        elif self.min_stack.top() >= value:
            self.min_stack.push(value)
        self.stack.push(value)
        self.end += 1

    def pop(self) -> None:
        if self.end != -1:
            if self.stack.top() == self.min_stack.top():
                self.min_stack.pop()

            self.stack.pop()
            self.end -= 1

    def top(self) -> int:
        return self.stack.top()

    def getMin(self) -> int:
        return self.min_stack.top()