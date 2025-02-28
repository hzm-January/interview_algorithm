class MinStack:

    def __init__(self):
        self.stack1 = []  # store element
        self.stack2 = []  # store minimum value

    def push(self, val: int) -> None:
        self.stack1.append(val)
        if self.stack2:
            val = min(self.stack2[-1], val)
        self.stack2.append(val)

    def pop(self) -> None:
        self.stack2.pop()
        self.stack1.pop()

    def top(self) -> int:
        return self.stack1[-1]

    def getMin(self) -> int:
        return self.stack2[-1]

# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
