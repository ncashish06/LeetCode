class Solution:
    # Date Solved: 12 April 2026, Sunday
    def missingNumber(self, nums: List[int]) -> int:
        """
        n = len(nums)
        total_sum = n * (n + 1) // 2  # Gauss' Formula
        partial_sum = 0
        for i in range(n):
            partial_sum += nums[i]

        return total_sum - partial_sum
        """

        """
        Bitwise XOR
        XOR is commutative and associative (order does not matter)
        If we XOR all numbers from 0 to n and all numbers present in the array, every number that appears in both places will cancel out, leaving only the missing number.

        missing = 4∧(0∧0)∧(1∧1)∧(2∧3)∧(3∧4)
                = (4∧4)∧(0∧0)∧(1∧1)∧(3∧3)∧2
                = 0∧0∧0∧0∧2
                = 2
        """

        missing = len(nums)
        for i, num in enumerate(nums):
            missing ^= i ^ num
        return missing
