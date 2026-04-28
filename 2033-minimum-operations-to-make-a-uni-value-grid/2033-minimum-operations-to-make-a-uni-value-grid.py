class Solution:
    # Date Solved: 27 April 2026, Monday
    # Time:  O(m*n log(m*n)) for sorting, Space: O(m*n)
    def minOperations(self, grid: List[List[int]], x: int) -> int:
        # Flatten 2D grid to 1D since grid structure doesn't matter
        # Here rows/columns are irrelevant, just the values
        nums = []
        for row in grid:
            for val in row:
                nums.append(val)

        # To get from value A to value B: (B - A) must be divisible by x
        # Therefore, all elements must have same remainder mod x
        remainder = nums[0] % x
        for num in nums:
            if num % x != remainder:
                return -1

        # Mean: minimizes sum of SQUARED differences,
        # Median: minimizes sum of ABSOLUTE differences (needed here)
        nums.sort()
        median = nums[len(nums) // 2]

        # Count total operations
        operations = 0
        for num in nums:
            operations += abs(num - median) // x

        return operations
