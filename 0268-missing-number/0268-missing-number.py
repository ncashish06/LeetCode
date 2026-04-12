class Solution:
    # Date Solved: 12 April 2026, Sunday
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        total_sum = n * (n + 1) // 2
        partial_sum = 0
        for i in range(n):
            partial_sum += nums[i]

        return total_sum - partial_sum
