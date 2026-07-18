class Solution:
    # Date Solved: 18 July 2026, Saturday, POTD
    # Time: O(n+log M) where n=length of nums array, and M=Maximum value in nums
    # O(n) time for finding max/min values, and O(logM) time for gcd of max/min values.
    # Space: O(1)
    def findGCD(self, nums: List[int]) -> int:
        a, b = min(nums), max(nums)
        while b:
            a, b = b, a % b  # Euclidean or division algorithm
        return a
