class Solution:
    # Date Solved: 13 April 2026, Monday
    def isPowerOfTwo(self, n: int) -> bool:
        """
        if n == 1:
            return True
        elif n < 1 or n % 2 != 0:
            return False
        return self.isPowerOfTwo(n // 2)
        """
        # Bitwise AND operator
        # if n <= 0:
        #     return False
        # return n & (-n) == n

        if n <= 0:
            return False
        return n & (n - 1) == 0
