class Solution:
    def reverse(self, x: int) -> int:
        sign = -1 if x < 0 else 1
        x = abs(x)
        rev = 0
        LIMIT = 2**31
        while x:
            x, mod = divmod(x, 10)
            rev = rev * 10 + mod
            if rev > LIMIT - 1:
                return 0
        return sign * rev