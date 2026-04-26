class Solution:
    # Date Solved: 26 April 2026, Sunday
    def isPowerOfFour(self, n: int) -> bool:
        """
        # Brute Force. Time: O(log n), Space: O(1)
        if n <= 0:
            return False

        x = 1
        while x < n:
            x *= 4
        return x == n

        # Top down recursion. Time: O(log n), Space: O(log n) for stack
        if n == 1:
            return True
        if n <= 0 or n % 4:
            return False
        return self.isPowerOfFour(n // 4)

        # Iteration: Same logic as recursion, but with a loop. Time: O(log n), Space: O(1)
        if n < 0:
            return False

        while n > 1:
            if n % 4:
                return False
            n //= 4

        return n == 1

        # Bitwise AND operator: Powers of four when divided by 3 leave remainder of 1. Time: O(1), Space: O(1)
        if n <= 0:
            return False
        return (n & (n - 1)) == 0 and (n % 3 == 1)
        """
        # Bit manipulation: Exactly one set bit and bit is at an even position. Time: O(1), Space: O(1)
        if n <= 0:
            return False
        for i in range(0, 32, 2):
            if n == (1 << i):
                return True
        return False
