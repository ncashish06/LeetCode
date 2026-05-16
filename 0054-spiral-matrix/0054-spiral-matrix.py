class Solution:
    # Date Solved: 15 May 2026, Friday
    # Blind 75 Question
    # This is similar to LC.2061 Number of Spaces Cleaning Robot Cleaned
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]  # right, down, left, up
        rows, cols = len(matrix), len(matrix[0])

        result = []
        visited = set()
        row, col, direction = 0, 0, 0  # start at top-left, facing right

        for _ in range(rows * cols):
            result.append(matrix[row][col])
            visited.add((row, col))

            next_row, next_col = (
                row + directions[direction][0],
                col + directions[direction][1],
            )

            # Turn if next cell is out of bounds OR already visited
            if (
                not (0 <= next_row < rows and 0 <= next_col < cols)
                or (next_row, next_col) in visited
            ):
                direction = (direction + 1) % 4
                next_row, next_col = (
                    row + directions[direction][0],
                    col + directions[direction][1],
                )

            row, col = next_row, next_col

        return result
