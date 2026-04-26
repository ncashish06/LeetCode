class Solution:
    # Date Solved: 25 April 2026, Saturday
    # Refer: Programming Live with Larry
    def containsCycle(self, grid: List[List[str]]) -> bool:
        rows = len(grid)
        cols = len(grid[0])
        visited = [[False] * cols for _ in range(rows)]
        has_cycle = False

        def dfs(row, col, parent_row, parent_col):
            nonlocal has_cycle
            visited[row][col] = True

            for dr, dc in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
                neighbor_row, neighbor_col = row + dr, col + dc
                if (
                    0 <= neighbor_row < rows
                    and 0 <= neighbor_col < cols
                    and grid[neighbor_row][neighbor_col] == grid[row][col]
                    and not (neighbor_row == parent_row and neighbor_col == parent_col)
                ):
                    if visited[neighbor_row][neighbor_col]:
                        has_cycle = True
                    else:
                        dfs(neighbor_row, neighbor_col, row, col)

        for r in range(rows):
            for c in range(cols):
                if not visited[r][c] and not has_cycle:
                    dfs(r, c, -1, -1)  # -1 because "no parent" for the starting cell

        return has_cycle
