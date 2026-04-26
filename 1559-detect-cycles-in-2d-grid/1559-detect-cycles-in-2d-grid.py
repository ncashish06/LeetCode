class Solution:
    # Date Solved: 25 April 2026, Saturday
    # Refer: Programming Live with Larry
    def containsCycle(self, grid: List[List[str]]) -> bool:
        rows = len(grid)
        cols = len(grid[0])
        visited = [[False] * cols for _ in range(rows)]
        cycle_found = False

        def dfs(x, y, px, py):
            visited[x][y] = True
            nonlocal cycle_found
            for dx, dy in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
                nx, ny = x + dx, y + dy
                if (
                    0 <= nx < rows
                    and 0 <= ny < cols
                    and grid[nx][ny] == grid[x][y]
                    and not (nx == px and ny == py)
                ):
                    if visited[nx][ny]:
                        cycle_found = True
                    else:
                        dfs(nx, ny, x, y)

        for x in range(rows):
            for y in range(cols):
                if not visited[x][y] and not cycle_found:
                    dfs(x, y, -1, -1)

        return cycle_found
