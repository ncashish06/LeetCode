from collections import deque


class Solution:
    # Date Solved: 1 July 2026, Wednesday, POTD
    # Solve LC.286 Walls and Gates (Medium) and LC.778 Swim in Rising Water (Hard) before this. Both are in NC150.
    # Refer: codestorywithMIK (NeetCode approach bit complex)
    # Multiple Topics covered here: BFS, Multi-Source BFS and Binary Search.  Can also be solved using Dijkstra's as this is single source shortest path problem.
    # Time: O(N*N*logN), Space: O(N*N)
    def maximumSafenessFactor(self, grid: List[List[int]]) -> int:
        n = len(grid)
        directions = [(1, 0), (-1, 0), (0, -1), (0, 1)]

        # Step 1: Multi-source BFS to compute distance to nearest thief for each cell
        distNearestThief = [[-1] * n for _ in range(n)]
        visited = [[False] * n for _ in range(n)]
        queue = deque()

        for i in range(n):
            for j in range(n):
                if grid[i][j] == 1:
                    queue.append((i, j))
                    visited[i][j] = True

        level = 0
        while queue:
            size = len(queue)
            for _ in range(size):
                curr_i, curr_j = queue.popleft()
                distNearestThief[curr_i][curr_j] = level

                for di, dj in directions:
                    new_i, new_j = curr_i + di, curr_j + dj
                    if 0 <= new_i < n and 0 <= new_j < n and not visited[new_i][new_j]:
                        queue.append((new_i, new_j))
                        visited[new_i][new_j] = True
            level += 1

        # Step 2: Helper to check if a path exists with given safeness factor
        def check(sf: int) -> bool:
            if distNearestThief[0][0] < sf:
                return False

            bfs_queue = deque([(0, 0)])
            local_visited = [[False] * n for _ in range(n)]
            local_visited[0][0] = True

            while bfs_queue:
                curr_i, curr_j = bfs_queue.popleft()

                if curr_i == n - 1 and curr_j == n - 1:
                    return True

                for di, dj in directions:
                    new_i, new_j = curr_i + di, curr_j + dj
                    if (
                        0 <= new_i < n
                        and 0 <= new_j < n
                        and not local_visited[new_i][new_j]
                    ):
                        if distNearestThief[new_i][new_j] < sf:
                            continue  # reject this cell
                        bfs_queue.append((new_i, new_j))
                        local_visited[new_i][new_j] = True

            return False

        # Step 3: Binary search on the safeness factor
        l, r = 0, 400
        result = 0

        while l <= r:
            mid_sf = l + (r - l) // 2

            if check(mid_sf):
                result = mid_sf
                l = mid_sf + 1
            else:
                r = mid_sf - 1

        return result
