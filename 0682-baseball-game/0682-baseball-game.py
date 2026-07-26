class Solution:
    # Date Solved: 26 July 2026, Saturday
    # NC250
    # Refer: NeetCode
    def calPoints(self, operations: List[str]) -> int:
        """
        # Approach-1: 2 passes
        stack = []
        for op in operations:
            if op == "+":
                stack.append(stack[-1] + stack[-2])
            elif op == "D":
                stack.append(2 * stack[-1])
            elif op == "C":
                stack.pop()
            else:
                stack.append(int(op))
        return sum(stack)
        """
        # Approach-2: 1 pass with running sum
        stack, res = [], 0
        for op in operations:
            if op == "+":
                res += (
                    stack[-1] + stack[-2]
                )  # order matters, can't do after appending to stack
                stack.append(stack[-1] + stack[-2])
            elif op == "D":
                res += 2 * stack[-1]  # order matters, can't do after appending to stack
                stack.append(2 * stack[-1])
            elif op == "C":
                res -= stack.pop()  # order matters, can't do after appending to stack
            else:
                res += int(op)  # order matters, can't do after appending to stack
                stack.append(int(op))
        return res
