class Solution:
    # Date Solved: 23 July 2026, Thursday
    # POTD of 20 July 2026, Monday (Unsolved due to Bari trip)
    # In NC All
    # Refer: codestorywithMIK. He solves "LC. 189 Rotate Array" first and then this in the same video.
    """
    Approach for LC189 Rotate Array is 3 Reversals: Reverse entire array, Reverse first k elements and Reverse remaining elements.
    Here, assume you have elements in 1D array. If you want [row, col] mapping in 2D array:
    row = i / cols, col = idx % cols
    """

    # Time: O(n), n = row*col, Space : O(1)
    def shiftGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        """
        # Approach 1: Convert to 1D and then convert back
        # Refer: NeetCode editorial (not video)
        # After converting to 1D, solution is same as LC. 189 Rotate Array
        # Time: O(rows*cols), Space : O(rows*cols)
        rows, cols = len(grid), len(grid[0])
        n = rows * cols
        k = k % n

        arr = [0] * n
        for r in range(rows):
            for c in range(cols):
                arr[r * cols + c] = grid[r][c]

        def reverse(l, r):
            while l < r:
                arr[l], arr[r] = arr[r], arr[l]
                l += 1
                r -= 1

        reverse(0, n - 1)
        reverse(0, k - 1)
        reverse(k, n - 1)

        for r in range(rows):
            for c in range(cols):
                grid[r][c] = arr[r * cols + c]

        return grid
        """
        # Approach 2: In place solution by codestorywithMIK
        # Time: O(rows*cols), Space : O(1)
        rows, cols = len(grid), len(grid[0])
        n = rows * cols

        k = k % n
        # If k is a multiple of n, after k rotations, nums remains same. So, don't waste efforts.
        if k == 0:
            return grid

        def reverse(i, j):
            while i < j:
                row_i, col_i = i // cols, i % cols
                row_j, col_j = j // cols, j % cols
                grid[row_i][col_i], grid[row_j][col_j] = (
                    grid[row_j][col_j],
                    grid[row_i][col_i],
                )
                i += 1
                j -= 1

        reverse(0, n - 1)
        reverse(0, k - 1)
        reverse(k, n - 1)

        return grid
