class Solution:
    # Date Solved: 25 July 2026, Saturday, POTD
    # Refer: NC Ashish
    def maxProduct(self, n: int) -> int:
        digits = []
        while n:
            digit = n % 10
            n //= 10
            digits.append(digit)
        digits.sort(reverse=True)
        return digits[0] * digits[1]
