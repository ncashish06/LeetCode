class Solution:
    # Date Solved: 13 April 2026, Monday
    def isPowerOfTwo(self, n: int) -> bool:
        """
        # Brute Force. Time: O(log n), Space: O(1)
        if n <= 0:
            return False

        x = 1
        while x < n:
            x *= 2
        return x == n
        
        # Top down recursion. Time: O(log n), Space: O(log n) for stack
        if n == 1:
            return True
        elif n <= 0 or n % 2 == 1:
            return False
        return self.isPowerOfTwo(n // 2)
        
        # Iteration: Same logic as recursion, but with a loop. Time: O(log n), Space: O(1)
        if n <= 0:
            return False

        while n % 2 == 0:
            n >>= 1
        return n == 1
        """
        # Bitwise AND operator: Get/Isolate the Rightmost 1-bit. Time: O(1), Space: O(1)
        if n <= 0:
            return False
        return n & (-n) == n
        """
        # Bitwise AND operator: Turn off the Rightmost 1-bit. Time: O(1), Space: O(1)
        if n <= 0:
            return False
        return n & (n - 1) == 0
        
        # Smaller power of 2 must divide into 2^30 (largest 2 power in 32-bit signed integer)
        # Time: O(1), Space: O(1)
        if n <= 0:
            return False
        return ((1 << 30) % n) == 0
        """
