class Solution:
    from collections import deque

    def colorGrid(self, n: int, m: int, sources: list[list[int]]) -> list[list[int]]:
        # Initialize grid with 0 (uncolored)
        grid = [[0] * m for _ in range(n)]
        queue = deque()

        # Populate initial sources
        for r, c, color in sources:
            grid[r][c] = color
            queue.append((r, c))

        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

        while queue:
            # next_level_candidates stores (r, c) -> max_color found this step
            next_level_candidates = {}

            # Process all cells at the current time step
            for _ in range(len(queue)):
                r, c = queue.popleft()
                current_color = grid[r][c]

                for dr, dc in directions:
                    nr, nc = r + dr, c + dc

                    # Check bounds and if the cell is currently uncolored
                    if 0 <= nr < n and 0 <= nc < m and grid[nr][nc] == 0:
                        # Update the maximum color reaching this cell at this time step
                        if (
                            (nr, nc) not in next_level_candidates
                            or current_color > next_level_candidates[(nr, nc)]
                        ):
                            next_level_candidates[(nr, nc)] = current_color

            # After checking all neighbors, apply the colors and add to queue
            for (r, c), color in next_level_candidates.items():
                grid[r][c] = color
                queue.append((r, c))

        return grid
