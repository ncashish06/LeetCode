class Solution:
    # Date Solved: 30 August 2026, Sunday
    # Refer: Namaste DSA
    # NC250
    # Time: O(logx), Space: O(1)
    def mySqrt(self, x: int) -> int:
        if x < 2:
            return x
        l, r = 2, x // 2
        while l <= r:
            m = l + (r - l) // 2
            if m * m == x:
                return m
            elif m * m > x:
                r = m - 1
            else:
                l = m + 1
        return r
