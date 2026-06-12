from collections import deque


class Solution:
    # Date Solved: 12 June 2026, Friday
    # NC250
    # Refer: codestorywithMIK
    # Unlike in LC. 200 Number of Islands and LC. 695 Max Area of Island, here there is only one island.
    # Similar code in LC. 200 Number of Islands and LC. 695 Max Area of Island.
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        # Approach 1: Most intuitive and simple, without DFS or BFS
        # Time: O(m*n), Space: O(1)
        rows = len(grid)
        cols = len(grid[0])
        perimeter = 0

        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == 0:
                    continue

                if row - 1 < 0 or grid[row - 1][col] == 0:  # up
                    perimeter = perimeter + 1

                if row + 1 >= rows or grid[row + 1][col] == 0:  # down
                    perimeter = perimeter + 1

                if col - 1 < 0 or grid[row][col - 1] == 0:  # left
                    perimeter = perimeter + 1

                if col + 1 >= cols or grid[row][col + 1] == 0:  # right
                    perimeter = perimeter + 1

        return perimeter
        """
        # Approach 2: DFS
        # Time: O(m*n), Space: O(m*n) recursion stack
        rows = len(grid)
        cols = len(grid[0])
        self.perimeter = 0

        def dfs(row, col):
            if row < 0 or row >= rows or col < 0 or col >= cols or grid[row][col] == 0:
                self.perimeter = self.perimeter + 1
                return
            if grid[row][col] == -1:
                return

            grid[row][col] = -1  # mark visited

            dfs(row + 1, col)
            dfs(row - 1, col)
            dfs(row, col + 1)
            dfs(row, col - 1)

        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == 1:
                    dfs(row, col)
                    return self.perimeter

        return -1
        
        # Approach 3: BFS
        # Time: O(m*n), Space: O(m*n)
        rows = len(grid)
        cols = len(grid[0])
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        def bfs(start_row, start_col):
            perimeter = 0
            queue = deque()
            queue.append((start_row, start_col))
            grid[start_row][start_col] = -1

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
                        or grid[next_row][next_col] == 0
                    ):
                        perimeter = perimeter + 1
                    elif grid[next_row][next_col] == -1:
                        continue
                    else:
                        queue.append((next_row, next_col))
                        grid[next_row][next_col] = -1

            return perimeter

        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == 1:
                    return bfs(row, col)

        return -1
        """
