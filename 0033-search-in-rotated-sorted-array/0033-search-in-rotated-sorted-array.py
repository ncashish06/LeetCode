class Solution:
    # Date Solved: 21 May 2026, Thursday, POTD
    # Blind 75, Uses same logic from LC.153 Find Minimum in Rotated Sorted Array (Another Blind 75)
    # Refer: codestorywithMIK, Binary search problem
    def find_pivot(self, nums: list[int], l: int, r: int) -> int:
        # Exactly same code as LC.153 Find Minimum in Rotated Sorted Array
        """
        The key insight: always compare with nums[right].
        If nums[mid] > nums[right], the rotation (and thus the minimum) is to the RIGHT.
        Otherwise, the minimum is to the LEFT (including mid itself).
        Keep mid as a candidate (it could be the minimum), so don't do right = mid - 1
        """
        while l < r:
            mid = l + (r - l) // 2
            if nums[mid] > nums[r]:
                l = mid + 1
            else:
                r = mid
        return r

    def binary_search(self, nums: list[int], l: int, r: int, target: int) -> int:
        while l <= r:
            mid = l + (r - l) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                l = mid + 1
            else:
                r = mid - 1
        return -1

    def search(self, nums: list[int], target: int) -> int:
        n = len(nums)
        pivot = self.find_pivot(nums, 0, n - 1)

        if nums[pivot] == target:
            return pivot

        idx = self.binary_search(nums, pivot + 1, n - 1, target)
        if idx != -1:
            return idx

        idx = self.binary_search(nums, 0, pivot - 1, target)
        return idx
