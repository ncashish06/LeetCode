class Solution:
    # Date Solved: 8 May 2026, Friday
    # NC250
    """
    Approach: 3 Reversals
        1. Reverse entire array
        2. Reverse first k elements
        3. Reverse remaining elements

    Related Problems:
    - LC.48 Rotate Image (Blind 75):  Uses the same layer-by-layer ring traversal idea, but rotates a 2D matrix 90°.
    - LC.1914 Cyclically Rotating a Grid: Extracts each ring into a 1D array, then applies this exact 3-reversal logic.
    - LC. 1260 Shift 2D Grid (NC All): Refer codestorywithMIK's video.
    """

    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        # When k is larger than the array length n, rotating by k is the same as rotating by k % n.
        k = k % n

        def reverse(l, r):
            while l < r:
                nums[l], nums[r] = nums[r], nums[l]
                l, r = l + 1, r - 1

        reverse(0, n - 1)
        reverse(0, k - 1)
        reverse(k, n - 1)
