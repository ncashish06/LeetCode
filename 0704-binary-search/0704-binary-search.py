import bisect


class Solution:
    # Date Solved: 28 April 2026, Tuesday
    def search(self, nums: List[int], target: int) -> int:
        """
        # Iterative binary search
        left = 0
        right = len(nums) - 1
        while left <= right:
            # middle = middle = (left + right) // 2
            middle = left + ((right - left) // 2)  # Overflow safe version of above
            if nums[middle] == target:
                return middle
            elif target < nums[middle]:
                right = middle - 1
            else:
                left = middle + 1
        return -1

        # Upper bound
        idx = bisect.bisect_right(nums, target)
        if idx > 0 and nums[idx - 1] == target:
            return idx - 1
        else:
            return -1
        """
        # Lower bound
        idx = bisect.bisect_left(nums, target)
        if idx < len(nums) and nums[idx] == target:
            return idx
        else:
            return -1
