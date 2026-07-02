class Solution:
    # Date Solved: 2 July 2026, Thursday, POTD
    # Refer: codestorywithMIK's Graph Concepts & Qns Playlist
    def findSafeWalk(self, grid: List[List[int]], health: int) -> bool:
        """
        # Approach 1 - Using Dijkstra's
        # Time : O(E*logV) = O(m·n*log(m*n))
        # Space : O(m*n)
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        m, n = len(grid), len(grid[0])

        result = [[float("inf")] * n for _ in range(m)]
        result[0][0] = grid[0][0]  # Source = (0, 0)

        pq = [(result[0][0], 0, 0)]

        while pq:
            d, r, c = heapq.heappop(pq)

            if d > result[r][c]:
                continue

            for dr, dc in directions:
                nr, nc = r + dr, c + dc

                if nr < 0 or nr >= m or nc < 0 or nc >= n:
                    continue

                nd = d + grid[nr][nc]
                if nd < result[nr][nc]:
                    result[nr][nc] = nd
                    heapq.heappush(pq, (nd, nr, nc))

        return health - result[m - 1][n - 1] >= 1
        """
        # Approach 2 - Using 0-1 BFS
        # Time : O(m*n)
        # Space : O(m*n)
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        m, n = len(grid), len(grid[0])

        result = [[float("inf")] * n for _ in range(m)]
        result[0][0] = grid[0][0]  # source (0, 0)

        dq = deque()
        dq.appendleft((0, 0))

        while dq:
            r, c = dq.popleft()

            for dr, dc in directions:
                nr, nc = r + dr, c + dc

                if nr < 0 or nr >= m or nc < 0 or nc >= n:
                    continue

                nd = result[r][c] + grid[nr][nc]
                if nd < result[nr][nc]:
                    result[nr][nc] = nd
                    if grid[nr][nc] == 0:
                        dq.appendleft((nr, nc))
                    else:
                        dq.append((nr, nc))

        return health - result[m - 1][n - 1] >= 1
