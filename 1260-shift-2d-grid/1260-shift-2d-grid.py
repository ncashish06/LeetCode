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

    def shiftGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        row = len(grid)
        col = len(grid[0])
        n = row * col

        k = k % n
        # If k is a multiple of n, after k rotations, nums remains same. So, don't waste efforts.
        if k == 0:
            return grid

        def reverse(i, j):
            while i < j:
                row_i, col_i = i // col, i % col
                row_j, col_j = j // col, j % col
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
