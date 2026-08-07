class Solution:
    # Date Solved: 6 August 2026, Thursday, POTD
    # Time: O(log(n))
    def smallestNumber(self, n: int, t: int) -> int:
        def digit_product(num):
            product = 1
            while num:  # Time: O(digits) = O(log10(num))
                product *= num % 10
                if product == 0:
                    return 0
                num //= 10
            return product

        for i in range(n, n + 10):  # Time: O(10)
            if digit_product(i) % t == 0:  # Time: O(digits) = O(log10(num))
                return i
        # Not needed for correctness of the algorithm, but good practice to leave in for type-safety.
        return -1
