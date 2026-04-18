class Solution:
    def reverse(self, x: int) -> int:
        rev = 0
        while x:
            x, mod = divmod(x, 10)
            rev = rev * 10 + mod
        return rev

    def mirrorDistance(self, n: int) -> int:
        return abs(n - self.reverse(n))
