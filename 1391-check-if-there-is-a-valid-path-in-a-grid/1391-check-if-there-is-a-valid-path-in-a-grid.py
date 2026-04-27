from collections import deque


class Solution:
    def hasValidPath(self, grid: List[List[int]]) -> bool:
        rows, cols = len(grid), len(grid[0])

        # For each direction: (dr, dc, exits_needed, enters_needed)
        # RIGHT: current must have right-exit, neighbor must have left-entry
        # DOWN:  current must have down-exit,  neighbor must have up-entry
        # LEFT:  current must have left-exit,  neighbor must have right-entry
        # UP:    current must have up-exit,    neighbor must have down-entry

        right_exit = {1, 4, 6}
        left_exit = {1, 3, 5}
        down_exit = {2, 3, 4}
        up_exit = {2, 5, 6}

        # direction -> (dr, dc, required exit from cur, required entry into neighbor)
        directions = [
            (0, 1, right_exit, left_exit),  # moving right
            (0, -1, left_exit, right_exit),  # moving left
            (1, 0, down_exit, up_exit),  # moving down
            (-1, 0, up_exit, down_exit),  # moving up
        ]

        visited = [[False] * cols for _ in range(rows)]
        visited[0][0] = True
        queue = deque([(0, 0)])

        while queue:
            row, col = queue.popleft()

            # Reached destination!
            if row == rows - 1 and col == cols - 1:
                return True

            for dr, dc, exit_set, entry_set in directions:
                nr, nc = row + dr, col + dc

                if (
                    0 <= nr < rows
                    and 0 <= nc < cols
                    and not visited[nr][nc]
                    and grid[row][col] in exit_set  # current can exit this way
                    and grid[nr][nc] in entry_set   # neighbor can enter from this way
                ):  

                    visited[nr][nc] = True
                    queue.append((nr, nc))

        return False
