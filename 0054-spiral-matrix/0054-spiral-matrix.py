class Solution:
    # Date Solved: 15 May 2026, Friday
    # Blind 75 Question
    # This is similar to LC.2061 Number of Spaces Cleaning Robot Cleaned
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]  # right, down, left, up
        rows, cols = len(matrix), len(matrix[0])

        result = []
        visited = set()
        r, c, d = 0, 0, 0

        for _ in range(rows * cols): 
            result.append(matrix[r][c])
            visited.add((r, c))

            nr, nc = r + dirs[d][0], c + dirs[d][1]

            # Turn if next cell is out of bounds OR already visited
            if not (0 <= nr < rows and 0 <= nc < cols) or (nr, nc) in visited:
                d = (d + 1) % 4
                nr, nc = r + dirs[d][0], c + dirs[d][1]

            r, c = nr, nc

        return result
