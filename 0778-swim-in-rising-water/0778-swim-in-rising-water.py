from collections import deque
import heapq


class Solution:
    # Date Solved: 1 July 2026, Wednesday
    # NC150
    # One component of today's POTD is based on this. Today's POTD LC. 2812 covers multiple topics: BFS, Multi-Source BFS and Binary Search
    # Whenever a problem says something like "Minimize the maximum" or "Maximize the minimum", you will use Binary Search in that problem. This problem can also be solved using Dijkstra's as it is a Single Source Shortest Path problem.
    # Refer: codestorywithMIK
    def swimInWater(self, grid: List[List[int]]) -> int:
        # Approach 1: BFS + Binary Search
        # l = 0 and r = max(grid[i][j]) = n^2-1
        # Time: O(n^2 log n) — binary search over O(n^2) possible values, each BFS is O(n^2)
        # Space: O(n^2) for visited and the queue
        n = len(grid)
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        def reachable(mid: int) -> bool:
            if grid[0][0] > mid:
                return False

            visited = [[False] * n for _ in range(n)]
            queue = deque([(0, 0)])
            visited[0][0] = True

            while queue:
                i, j = queue.popleft()
                if i == n - 1 and j == n - 1:
                    return True

                for di, dj in directions:
                    ni, nj = i + di, j + dj
                    if (
                        0 <= ni < n
                        and 0 <= nj < n
                        and not visited[ni][nj]
                        and grid[ni][nj] <= mid
                    ):
                        visited[ni][nj] = True
                        queue.append((ni, nj))

            return False

        l, r = grid[0][0], n * n - 1
        result = 0

        while l <= r:
            mid = l + (r - l) // 2
            if reachable(mid):
                result = mid
                r = mid - 1
            else:
                l = mid + 1

        return result
        """
        # Approach 2: Dijkstra's Algorithm
        # shortest-path problem where the "cost" to enter a cell is max(current_time, grid[cell]). Use a min-heap to always expand the currently cheapest reachable cell first.
        # Time: O(n^2 log n) — each cell can be pushed multiple times, and heap operations are O(log(n^2)) = O(log n).
        # Space: O(n^2) for result and the heap.
        n = len(grid)
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        result = [[float("inf")] * n for _ in range(n)]
        result[0][0] = grid[0][0]

        pq = [(grid[0][0], 0, 0)]  # (time, i, j)

        while pq:
            curr_time, i, j = heapq.heappop(pq)

            if i == n - 1 and j == n - 1:
                return curr_time

            if curr_time > result[i][j]:
                continue

            for di, dj in directions:
                ni, nj = i + di, j + dj
                if 0 <= ni < n and 0 <= nj < n:
                    next_time = max(curr_time, grid[ni][nj])
                    if next_time < result[ni][nj]:
                        result[ni][nj] = next_time
                        heapq.heappush(pq, (next_time, ni, nj))

        return -1  # should never reach here
        """
