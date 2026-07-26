class Solution:
    # Date Solved: 26 July 2026, Sunday
    # NC250
    # Refer: codestorywithMIK and NeetCode
    # Similar to "LC20. Valid Parentheses" with different magnitudes
    # Time: O(n), Space: O(n)
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []

        for a in asteroids:
            # A single incoming asteroid can destroy multiple asteroids on the stack. You need a loop.
            while stack and a < 0 and stack[-1] > 0:
                diff = a + stack[-1]
                if diff < 0:
                    stack.pop()
                elif diff > 0:
                    a = 0
                    break
                else:
                    stack.pop()
                    a = 0

            if a:
                stack.append(a)

        return stack
