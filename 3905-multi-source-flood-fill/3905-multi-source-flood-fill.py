from collections import deque

class Solution:
    # Date Solved: 26 April 2026, Sunday
    # Multi-source BFS problem
    def colorGrid(self, n: int, m: int, sources: list[list[int]]) -> list[list[int]]:
        # Initialize grid with 0 (uncolored)
        grid = [[0] * m for _ in range(n)]
        queue = deque()

        for r, c, color in sources:
            grid[r][c] = color
            queue.append((r, c))

        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

        while queue:
            # key: (row, col), value: max_color_seen_so_far, to handle simultaneous arrivals
            potential_fills = {}

            for _ in range(len(queue)): # Standard BFS uses a simple while queue loop. However, to handle simultaneous events, we must process the queue in levels (using len(queue)).
                curr_r, curr_c = queue.popleft()
                current_color = grid[curr_r][curr_c]

                for dr, dc in directions:
                    next_r, next_c = curr_r + dr, curr_c + dc
                    if (0 <= next_r < n and 0 <= next_c < m and grid[next_r][next_c] == 0):
                        # When multiple "agents" (colors) compete for the same resource (a cell) at the exact same time, you cannot update the global state (the grid) immediately.
                        # Dictionary here acts like a staging (temporary buffer) area.
                        if (next_r,next_c) not in potential_fills or current_color > potential_fills[(next_r, next_c)]:
                            # Throughout this whole step, the actual stays 0. This ensures both sources see the cell as "uncolored" and have a fair chance to compete for it.
                            potential_fills[(next_r, next_c)] = current_color

            # After checking all neighbors, apply the colors and add to queue
            for (r, c), final_color in potential_fills.items():
                grid[r][c] = final_color
                queue.append((r, c))

        return grid
