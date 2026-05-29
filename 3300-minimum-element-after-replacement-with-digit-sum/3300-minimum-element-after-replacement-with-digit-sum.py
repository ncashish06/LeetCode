class Solution:
    # Date Solved: 29 May 2026, Friday, POTD
    def minElement(self, nums: List[int]) -> int:
        # Approach 1:  Time: O(n * log10(m)) here log10(m) factor is at most 4 iterations given the constraints, Space: O(1)
        def digit_sum(n):
            total = 0
            while n > 0:
                total += n % 10
                n //= 10
            return total

        return min(digit_sum(num) for num in nums)

        # Approach 2: Pythonic solution
        # return min(sum(int(d) for d in str(num)) for num in nums)
