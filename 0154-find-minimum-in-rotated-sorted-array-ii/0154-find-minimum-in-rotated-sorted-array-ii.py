class Solution:
    # Date Solved: 15 May 2026, Friday
    # Previous LC153. Blind 75 question, Problem of the day
    # Refer: codestorywithMIK, Binary search problem
    def findMin(self, nums: List[int]) -> int:
        """
        The key insight: always compare with nums[right].
        If nums[mid] > nums[right], the rotation (and thus the minimum) is to the RIGHT.
        Otherwise, the minimum is to the LEFT (including mid itself).
        Keep mid as a candidate (it could be the minimum), so don't do right = mid - 1
        """
        l, r = 0, len(nums) - 1
        result_idx = 0

        while l <= r:
            # Remove duplicates from left
            while l < r and nums[l] == nums[l + 1]:
                l += 1

            # Remove duplicates from right
            while l < r and nums[r] == nums[r - 1]:
                r -= 1

            mid = l + (r - l) // 2

            # Update answer
            if nums[mid] < nums[result_idx]:
                result_idx = mid

            # Minimum lies on right side
            if nums[mid] > nums[r]:
                l = mid + 1
            # Minimum can be on left side
            else:
                r = mid - 1

        return nums[result_idx]