class Solution:
    # Date Solved: 26 May 2026, Tuesday
    # Blind 75
    # Refer: structy.net or Alvin The Programmer YouTube
    def isValid(self, s: str) -> bool:
        matching_symbol = {"(": ")", "[": "]", "{": "}"}

        stack = []  # tracks expected closing brackets in order

        for ch in s:
            if ch in matching_symbol:
                # Current char is an opening bracket;
                # push its expected closing bracket onto the stack
                stack.append(matching_symbol[ch])
            else:
                # Current char is a closing bracket;
                # check if it matches the most recent expected closing bracket
                if not stack or stack[-1] != ch:
                    # Stack is empty (no matching open bracket)
                    # or top of stack doesn't match -> invalid
                    return False
                else:
                    # Correct closing bracket found; pop the expectation
                    stack.pop()

        # Valid only if all opening brackets were properly closed
        return len(stack) == 0
