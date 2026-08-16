# Date Solved: 15 August 2026, Saturday, Weekly Premium W3
# Refer: Claude
class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        self.m = len(matrix)
        self.n = len(matrix[0])
        self.matrix = [[0] * self.n for _ in range(self.m)]  # tracks current values
        self.tree = [[0] * (self.n + 1) for _ in range(self.m + 1)]

        for i in range(self.m):
            for j in range(self.n):
                self.update(i, j, matrix[i][j])

    def update(self, row: int, col: int, val: int) -> None:
        delta = val - self.matrix[row][col]
        self.matrix[row][col] = val

        i = row + 1
        while i <= self.m:
            j = col + 1
            while j <= self.n:
                self.tree[i][j] += delta
                j += j & (-j)
            i += i & (-i)

    def _prefix_sum(self, row: int, col: int) -> int:
        # sum of matrix[0..row-1][0..col-1]
        total = 0
        i = row
        while i > 0:
            j = col
            while j > 0:
                total += self.tree[i][j]
                j -= j & (-j)
            i -= i & (-i)
        return total

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        return (
            self._prefix_sum(row2 + 1, col2 + 1)
            - self._prefix_sum(row1, col2 + 1)
            - self._prefix_sum(row2 + 1, col1)
            + self._prefix_sum(row1, col1)
        )


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# obj.update(row,col,val)
# param_2 = obj.sumRegion(row1,col1,row2,col2)
