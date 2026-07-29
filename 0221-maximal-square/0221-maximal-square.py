class Solution:
    # Date Solved: 28 July 2026, Tuesday
    # In NC All
    # Asked in "How to solve a Google coding interview question" YoutTube video on "Life at Google"
    # channel posted on 10 Feb 2025, Tuesday
    # codestorywithMIK's video is "Count Square Submatrices with All Ones" which is 102nd video of his
    # "DP: Popular Problems" playlist
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        """
        # Approach 1: Simple Recursion Memoization
        # Time: O(m*n), Space: O(m*n)
        self.rows = len(matrix)
        self.cols = len(matrix[0])
        t = [[-1] * self.cols for _ in range(self.rows)]

        def solve(i, j):
            if i >= self.rows or j >= self.cols:
                return 0

            if matrix[i][j] == "0":
                return 0

            if t[i][j] != -1:
                return t[i][j]

            # Right
            right = solve(i, j + 1)
            # Diagonal
            diagonal = solve(i + 1, j + 1)
            # Below
            below = solve(i + 1, j)

            t[i][j] = 1 + min(right, diagonal, below)
            return t[i][j]

        max_side = 0
        for i in range(self.rows):
            for j in range(self.cols):
                if matrix[i][j] == "1":
                    max_side = max(max_side, solve(i, j))

        return max_side * max_side
        """
        # Approach 2: Simple Bottom Up
        # Time: O(m*n), Space: O(m*n)
        if len(matrix) == 0:
            return 0

        rows = len(matrix)
        cols = len(matrix[0])

        t = [[0] * cols for _ in range(rows)]
        max_side = 0

        for i in range(rows):
            for j in range(cols):
                if i == 0 or j == 0:
                    t[i][j] = int(matrix[i][j])
                else:
                    if matrix[i][j] == "1":
                        # Because, if you have any 0, then you cannot expand side of square
                        t[i][j] = 1 + min(t[i - 1][j], t[i][j - 1], t[i - 1][j - 1])
                max_side = max(max_side, t[i][j])

        return max_side * max_side
