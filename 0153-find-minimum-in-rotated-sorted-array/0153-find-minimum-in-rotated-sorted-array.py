class Solution:
    # Date Solved: 14 May 2026, Thursday
    # Blind 75 question, Problem of the day
    # Refer: codestorywithMIK, Binary search problem
    def findMin(self, nums: List[int]) -> int:
        """
        The key insight: always compare with nums[right].
        If nums[mid] > nums[right], the rotation (and thus the minimum) is to the RIGHT.
        Otherwise, the minimum is to the LEFT (including mid itself).
        Keep mid as a candidate (it could be the minimum), so don't do right = mid - 1
        """
        left, right = 0, len(nums) - 1
        while left < right:
            mid = left + (right - left) // 2
            if nums[mid] > nums[right]:
                left = mid + 1
            else:
                right = mid
        return nums[left]
