class Solution:
    # Date Solved: 26 July 2026, Sunday, POTD
    def maximumProduct(self, nums: List[int]) -> int:
        # Approach 1: Solved on my own
        # Time: O(n log n), Space: O(1)
        nums.sort()
        # Case 1: three largest positive numbers
        candidate1 = nums[-1] * nums[-2] * nums[-3]
        # Case 2: two smallest (could be very negative) * largest
        candidate2 = nums[0] * nums[1] * nums[-1]
        return max(candidate1, candidate2)
