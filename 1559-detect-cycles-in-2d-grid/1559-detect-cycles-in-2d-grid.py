from collections import deque


class Solution:
    # Date Solved: 25 April 2026, Saturday
    def containsCycle(self, grid: List[List[str]]) -> bool:
        rows, cols = len(grid), len(grid[0])
        visited = [[False] * cols for _ in range(rows)]

        def bfs(start_row, start_col):
            queue = deque()
            queue.append((start_row, start_col, -1, -1))
            visited[start_row][start_col] = True

            while queue:
                row, col, parent_row, parent_col = queue.popleft()

                for dr, dc in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                    neighbor_row, neighbor_col = row + dr, col + dc

                    if (
                        0 <= neighbor_row < rows
                        and 0 <= neighbor_col < cols
                        and grid[neighbor_row][neighbor_col] == grid[row][col]
                        and not (neighbor_row == parent_row and neighbor_col == parent_col)
                    ):

                        if visited[neighbor_row][neighbor_col]:
                            return True  # Cycle found!

                        visited[neighbor_row][neighbor_col] = True
                        queue.append((neighbor_row, neighbor_col, row, col))

            return False

        for r in range(rows):
            for c in range(cols):
                if not visited[r][c]:
                    if bfs(r, c):
                        return True

        return False
