class Solution:
    # Date Solved: 3 May 2026, Sunday
    """
    Refer: Part of NeetCode 250 solution
    Approach 1: Rotate By Four Cells — traverse each ring layer and cycle 4 cells at a time.
    Approach 2: Reverse + Transpose — reverse matrix vertically, then transpose.
    Note: Approach 1 only works cleanly here because k=1 (fixed 90° rotation), so elements can be cycled directly without extracting to 1D.
    Related Problems:
    - LC189  (Rotate Array):  The 1D rotation primitive. When k is variable, extract the ring to 1D and apply LC189.
    - LC1914 (Cyclically Rotating a Grid): Generalises Approach 1's ring traversal to support arbitrary k rotations using LC189.
    """

    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """

        # Approach 1: Rotate By Four Cells
        l = 0
        r = len(matrix[0]) - 1  # right = number of columns - 1
        while l < r:
            for i in range(r - l):
                top, bottom = l, r

                # save the topleft
                topLeft = matrix[top][l + i]

                # move bottom left into top left
                matrix[top][l + i] = matrix[bottom - i][l]

                # move bottom right into bottom left
                matrix[bottom - i][l] = matrix[bottom][r - i]

                # move top right into bottom right
                matrix[bottom][r - i] = matrix[top + i][r]

                # move top left into top right
                matrix[top + i][r] = topLeft
            r -= 1
            l += 1
        """
        # Approach 2: Reverse And Transpose
        # Reverse the matrix vertically
        matrix.reverse()

        # Transpose the matrix
        for i in range(len(matrix)):
            for j in range(i + 1, len(matrix)):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
        """
