class Solution:
    # Date Solved: 13 September 2026, Sunday
    # In NC All and B2Go
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        """
        # Approach 1: 2 passes
        # Time: O(n), Space:O(1)
        left = 0
        n = len(nums)
        for right in range(n):
            if nums[right] != 0:  # Keep moving non-zero elements before
                nums[left] = nums[right]
                left += 1

        for i in range(left, n):  # remaining slors filled by 0s
            nums[i] = 0
        """
        # Approach 2: 1 pass
        # Time: O(n), Space:O(1)
        left = 0
        for right in range(len(nums)):
            if nums[right] != 0:
                nums[left], nums[right] = nums[right], nums[left]
                left += 1
