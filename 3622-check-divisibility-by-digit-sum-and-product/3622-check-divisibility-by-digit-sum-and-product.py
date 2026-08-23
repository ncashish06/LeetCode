class Solution:
    # Date Solved: 22 August 2026, Saturday, POTD
    # Refer: LeetCode editorial
    # Time: O(logn) = O(number of digits), Space: O(1)
    def checkDivisibility(self, n: int) -> bool:
        digit_sum = 0
        digit_product = 1
        original = n
        while n > 0:
            digit = n % 10
            n //= 10
            digit_sum += digit
            digit_product *= digit
        return original % (digit_sum + digit_product) == 0
