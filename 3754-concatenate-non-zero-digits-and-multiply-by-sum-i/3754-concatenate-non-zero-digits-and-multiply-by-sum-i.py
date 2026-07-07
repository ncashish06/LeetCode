class Solution:
    # Date Solved: 7 July 2026, Tuesday, POTD
    def sumAndMultiply(self, n: int) -> int:
        x = 0
        total = 0
        pow10 = 1

        while n > 0:
            digit = n % 10
            total += digit

            if digit > 0:
                x = x + (digit * pow10)
                pow10 *= 10

            n //= 10

        return x * total
