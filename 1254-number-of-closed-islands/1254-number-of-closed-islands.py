class Solution:
    # Date Solved: 25 July 2026, Saturday
    # NC All
    # Refer: NC Ashish. codestorywithMIK and NeetCode do DFS.
    def closedIsland(self, grid: List[List[int]]) -> int:
        # Approach: BFS per unvisited land cell. For each land component, BFS through it fully. If ANY cell in that component touches the grid boundary, the island is NOT closed.
        # Time : O(rows * cols) - each cell visited at most once total
        # Space: O(rows * cols) - grid mutation acts as visited + queue

        rows, cols = len(grid), len(grid[0])
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

        def bfs(start_row, start_col):
            # Returns True if this land component is fully closed
            # (never touches the boundary), False otherwise
            is_closed = True
            que = deque()

            grid[start_row][start_col] = 1
            que.append((start_row, start_col))

            while que:
                i, j = que.popleft()

                # If this cell sits on the boundary, the island leaks off the grid
                if i == 0 or i == rows - 1 or j == 0 or j == cols - 1:
                    is_closed = False

                for di, dj in directions:
                    ni, nj = i + di, j + dj

                    if 0 <= ni < rows and 0 <= nj < cols:
                        if grid[ni][nj] == 0:  # unvisited land
                            grid[ni][nj] = 1  # mark visited
                            que.append((ni, nj))

            return is_closed

        count = 0
        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == 0:
                    if bfs(row, col):
                        count += 1

        return count
