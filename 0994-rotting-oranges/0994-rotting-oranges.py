class Solution:
    # Date Solved: 24 July 2026, Friday
    # NC150
    # Solved on my own. Multi-source BFS.
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        directions = [(0, 1), (1, 0), (-1, 0), (0, -1)]
        rotten_queue = deque()
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 2:
                    rotten_queue.append((r, c))

        minutes = 0
        while rotten_queue:
            rotted_this_round = False
            N = len(rotten_queue)
            for _ in range(N):
                curr_row, curr_col = rotten_queue.popleft()
                for dr, dc in directions:
                    next_row, next_col = curr_row + dr, curr_col + dc
                    if (
                        0 <= next_row < rows
                        and 0 <= next_col < cols
                        and grid[next_row][next_col] == 1
                    ):
                        grid[next_row][next_col] = 2
                        rotten_queue.append((next_row, next_col))
                        rotted_this_round = True

            if rotted_this_round:
                minutes += 1

        # Check for any fresh oranges left unrotten
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    return -1

        return minutes
