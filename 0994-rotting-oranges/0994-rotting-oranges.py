class Solution:
    from collections import deque

    def orangesRotting(self, grid: List[List[int]]) -> int:
        # The tricky part is determining when a minute has elapsed. To handle this, push adjacent neighbors along with the current minute information into the queue.

        rows = len(grid)
        cols = len(grid[0])

        rotten_oranges_queue = deque()
        fresh_orange_count = 0

        # Build queue with rotten oranges positions and count total fresh oranges
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 2:
                    rotten_oranges_queue.append((r, c, 0))
                elif grid[r][c] == 1:
                    fresh_orange_count += 1

        if fresh_orange_count == 0:
            return 0

        minutes_elapsed = 0

        while rotten_oranges_queue:
            curr_r, curr_c, time = rotten_oranges_queue.popleft()

            if curr_r > 0 and grid[curr_r - 1][curr_c] == 1:
                grid[curr_r - 1][curr_c] = 2
                fresh_orange_count -= 1
                rotten_oranges_queue.append((curr_r - 1, curr_c, time + 1))
            if curr_r < rows - 1 and grid[curr_r + 1][curr_c] == 1:
                grid[curr_r + 1][curr_c] = 2
                fresh_orange_count -= 1
                rotten_oranges_queue.append((curr_r + 1, curr_c, time + 1))
            if curr_c < cols - 1 and grid[curr_r][curr_c + 1] == 1:
                grid[curr_r][curr_c + 1] = 2
                fresh_orange_count -= 1
                rotten_oranges_queue.append((curr_r, curr_c + 1, time + 1))
            if curr_c > 0 and grid[curr_r][curr_c - 1] == 1:
                grid[curr_r][curr_c - 1] = 2
                fresh_orange_count -= 1
                rotten_oranges_queue.append((curr_r, curr_c - 1, time + 1))

            minutes_elapsed = max(minutes_elapsed, time)

        return minutes_elapsed if fresh_orange_count == 0 else -1
