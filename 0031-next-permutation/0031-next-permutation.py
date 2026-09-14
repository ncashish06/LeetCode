class Solution:
    # Date Solved: 13 September 2026, Sunday
    # In NC All and B2Go
    # Time: O(n), Space: O(1)
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        pivot = n - 2  # Last is neither increasing nor decreasing
        while pivot >= 0 and nums[pivot] >= nums[pivot + 1]:
            pivot -= 1  # Pivot is the first character from the right that breaks non-increasing order

        # If pivot is not found, the array is already in its largest permutation. In
        # this case, reverse the array to obtain the smallest permutation.
        if pivot == -1:
            nums.reverse()
            return

        # Find the rightmost successor to the pivot
        rightmost_successor = n - 1
        while nums[rightmost_successor] <= nums[pivot]:
            rightmost_successor -= 1

        # Swap the rightmost successor with the pivot to increase the lexicographical order of the suffix
        nums[pivot], nums[rightmost_successor] = (
            nums[rightmost_successor],
            nums[pivot],
        )

        # Reverse the suffix after the pivot to minimize its permutation
        nums[pivot + 1 :] = reversed(nums[pivot + 1 :])
