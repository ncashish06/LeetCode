from collections import deque


class Solution:
    # Date Solved: 1 July 2026, Wednesday
    # NC150
    # Solved on my own. Multi-source BFS, similar to Rotting Oranges
    # One component of today's POTD is based on this. Today's POTD LC. 2812 covers multiple topics: BFS, Multi-Source BFS and Binary Search
    # Time: O(r*c), Space: O(r*c)
    def wallsAndGates(self, rooms: List[List[int]]) -> None:
        """
        Do not return anything, modify rooms in-place instead.
        """
        rows, cols = len(rooms), len(rooms[0])
        queue = deque()
        directions = [(0, 1), (1, 0), (-1, 0), (0, -1)]
        INF = 2147483647

        for r in range(rows):
            for c in range(cols):
                if rooms[r][c] == 0:
                    queue.append((r, c))

        level = 1  # neighbors of gates are 1 step away
        while queue:
            n = len(queue)
            for _ in range(n):
                curr_r, curr_c = queue.popleft()
                for nr, nc in directions:
                    next_r, next_c = curr_r + nr, curr_c + nc
                    if (
                        0 <= next_r < rows
                        and 0 <= next_c < cols
                        and rooms[next_r][next_c]
                        == INF  # only walkable, unvisited rooms
                    ):
                        rooms[next_r][next_c] = level
                        queue.append((next_r, next_c))
            level += 1
