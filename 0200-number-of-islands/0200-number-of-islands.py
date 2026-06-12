from collections import deque


class Solution:
    # Date Solved: 12 June 2026, Friday
    # Blind 75
    # Refer: codestorywithMIK
    # Copy paste same solution as  in LC. 463 Island Perimeter with minor changes
    # Similar code in LC. 463 Island Perimeter and LC. 695 Max Area of Island.
    def numIslands(self, grid: List[List[str]]) -> int:
        """
        # Approach 1: DFS
        # Time: O(m*n), Space: O(m*n) recursion stack
        rows = len(grid)
        cols = len(grid[0])
        islands = 0

        def dfs(row, col):
            if (
                row < 0
                or row >= rows
                or col < 0
                or col >= cols
                or grid[row][col] != "1"
            ):
                return

            grid[row][col] = "$"  # mark visited

            dfs(row + 1, col)
            dfs(row - 1, col)
            dfs(row, col + 1)
            dfs(row, col - 1)

        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == "1":
                    dfs(row, col)
                    islands += 1

        return islands
        """
        # Approach 2: BFS
        # Time: O(m*n), Space: O(m*n)
        rows = len(grid)
        cols = len(grid[0])
        islands = 0
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        def bfs(start_row, start_col):
            queue = deque()
            queue.append((start_row, start_col))
            grid[start_row][start_col] = "$"

            while len(queue) > 0:
                current = queue.popleft()
                current_row = current[0]
                current_col = current[1]

                for direction in directions:
                    next_row = current_row + direction[0]
                    next_col = current_col + direction[1]

                    if (
                        next_row < 0
                        or next_row >= rows
                        or next_col < 0
                        or next_col >= cols
                        or grid[next_row][next_col] != "1"
                    ):
                        continue
                    else:
                        queue.append((next_row, next_col))
                        grid[next_row][next_col] = "$"

        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == "1":
                    bfs(row, col)
                    islands += 1
        return islands
