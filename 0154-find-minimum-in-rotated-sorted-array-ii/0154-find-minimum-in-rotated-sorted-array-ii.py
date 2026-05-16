class Solution:
    # Date Solved: 15 May 2026, Friday
    # Previous LC153. Blind 75 question, Problem of the day
    # Refer: codestorywithMIK, Binary search problem
    def findMin(self, nums: List[int]) -> int:
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

            if nums[mid] < nums[result_idx]:
                result_idx = mid
            if nums[mid] > nums[r]: # Minimum lies on right side
                l = mid + 1
            else:   # Minimum can be on left side
                r = mid - 1

        return nums[result_idx]