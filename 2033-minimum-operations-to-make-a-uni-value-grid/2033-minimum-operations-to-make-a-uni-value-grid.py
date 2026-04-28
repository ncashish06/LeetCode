class Solution:
    # Date Solved: 27 April 2026, Monday
    # Time: O(m*n log(m*n)) — dominated by sorting
    # Space: O(m*n) — flattened array
    def minOperations(self, grid: List[List[int]], x: int) -> int:
        # Flatten 2D grid into 1D — row/column positions are irrelevant,
        # only the values matter for this problem
        nums = []
        for row in grid:
            for val in row:
                nums.append(val)

        # Impossibility check:
        # Each operation adds or subtracts x, so to transform A -> B,
        # (B - A) must be divisible by x, which means A % x == B % x.
        # If any element has a different remainder, unification is impossible
        remainder = nums[0] % x
        for num in nums:
            if num % x != remainder:
                return -1

        # Mean: minimizes sum of SQUARED differences,
        # Median: minimizes sum of ABSOLUTE differences (needed here)
        nums.sort()
        median = nums[len(nums) // 2]

        operations = 0
        for num in nums:
            operations += abs(num - median) // x

        return operations
