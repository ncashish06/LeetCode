class Solution:
    # Date Solved: 25 July 2026, Saturday, POTD
    # Refer: NC Ashish
    def maxProduct(self, n: int) -> int:
        """
        # Approach 1: Solved on my own
        # Time: O(dlogd) where d = number of digits in n, Space: O(d)
        digits = []
        while n:
            digit = n % 10
            n //= 10
            digits.append(digit)
        digits.sort(reverse=True)
        return digits[0] * digits[1]
        """
        # Approach 2: Optimal
        # Time: O(logn), Space: O(1)
        max_digit, second_max_digit = 0, 0
        while n:
            digit = n % 10
            if digit > max_digit:
                max_digit, second_max_digit = digit, max_digit
            elif digit > second_max_digit:
                second_max_digit = digit
            n //= 10
        return max_digit * second_max_digit
