class Solution:
    # Date Solved: 28 April 2026, Tuesday
    def fib(self, n: int) -> int:
        """
        # Most inefficient approach
        # Time: O(2^n), Space: O(n).
        if n <= 1:
            return n
        return self.fib(n - 1) + self.fib(n - 2)

        # Non-DP, linear time approach
        a, b = 0, 1
        for _ in range(n):
            a, b = b, a + b
        return a
        """
        # Below approach is math based and most efficient method
        # Time: O(log n), Space: O(1). This solution is even better than  DP based approaches which are linear time.
        golden_ratio = (1 + (5**0.5)) / 2
        return int(round((golden_ratio**n) / (5**0.5)))
