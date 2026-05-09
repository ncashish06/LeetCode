class Solution:
    # Date Solved: 8 May 2026, Friday
    """
    Approach: Extract each ring -> rotate 1D array -> reinsert
    1. For each layer (concentric ring), extract elements clockwise into a 1D array.
    2. Rotate that array by k steps using LC189's 3-reversal trick.
    3. Write elements back to the grid in the same clockwise order.

    This problem is a direct combination of:
    - LC48  (Blind 75):      Ring/layer traversal pattern (top, bottom, left, right boundaries).
    - LC189 (NeetCode 250):  3-reversal k-step rotation applied to each extracted ring.

    Key insight: LC48 skips the 1D extraction because k=1 is fixed. LC1914 needs it because k is variable.
    """

    def rotateGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        m, n = len(grid), len(grid[0])

        def reverse(arr, l, r):
            while l < r:
                arr[l], arr[r] = arr[r], arr[l]
                l, r = l + 1, r - 1

        def rotate(arr, k):
            # Note: Unlike LC189 (right rotation), this requires LEFT rotation on the extracted ring.
            # Fix: use (-k) % size instead of k % size.
            size = len(arr)
            k = (-k) % size
            reverse(arr, 0, size - 1)
            reverse(arr, 0, k - 1)
            reverse(arr, k, size - 1)

        def extract(layer):
            # Extract clockwise: top -> right -> bottom -> left
            top, left = layer, layer
            bottom, right = m - 1 - layer, n - 1 - layer

            elements = []
            for c in range(left, right + 1):  # top row
                elements.append(grid[top][c])
            for r in range(top + 1, bottom + 1):  # right col
                elements.append(grid[r][right])
            for c in range(right - 1, left - 1, -1):  # bottom row
                elements.append(grid[bottom][c])
            for r in range(bottom - 1, top, -1):  # left col
                elements.append(grid[r][left])
            return elements

        def insert(layer, elements):
            # Place elements back in the same clockwise order
            top, left = layer, layer
            bottom, right = m - 1 - layer, n - 1 - layer

            idx = 0
            for c in range(left, right + 1):
                grid[top][c] = elements[idx]
                idx += 1
            for r in range(top + 1, bottom + 1):
                grid[r][right] = elements[idx]
                idx += 1
            for c in range(right - 1, left - 1, -1):
                grid[bottom][c] = elements[idx]
                idx += 1
            for r in range(bottom - 1, top, -1):
                grid[r][left] = elements[idx]
                idx += 1

        num_layers = min(m, n) // 2
        for layer in range(num_layers):
            elements = extract(layer)
            rotate(elements, k)
            insert(layer, elements)

        return grid
