class MinStack:
    # Date Solved: 26 July 2026, Sunday
    # NC150
    # LeetCode editorial best for this.
    def __init__(self):
        # Each element in the stack is a tuple: (value, min_so_far)
        self.stack = []

    def push(self, x: int) -> None:
        # If empty, x is both the value and the current minimum
        if not self.stack:
            self.stack.append((x, x))
            return
        # Otherwise, compare x with the min seen so far and store the smaller one
        current_min = self.stack[-1][1]
        self.stack.append((x, min(x, current_min)))

    def pop(self) -> None:
        # Removing the top tuple removes both the value and its min together
        self.stack.pop()

    def top(self) -> int:
        # First item of the tuple is the actual value
        return self.stack[-1][0]

    def getMin(self) -> int:
        # Second item of the tuple is the running minimum at this point
        return self.stack[-1][1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(value)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
