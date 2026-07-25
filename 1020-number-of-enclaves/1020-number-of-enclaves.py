class Solution:
    # Date Solved: 25 July 2026, Saturday
    # NC All
    # Refer: NC Ashish. codestorywithMIK and NeetCode do DFS.
    # NeetCode editorial has this Multi-Source BFS approach.
    def numEnclaves(self, grid: List[List[int]]) -> int:
        # Approach: Multi-Source BFS from land cells on the border. Any land cell reachable from the border can "walk off" the grid, so it's NOT an enclave. Everything else that's land IS an enclave.
        # Time : O(rows * cols) - each cell visited at most once
        # Space: O(rows * cols) - visited grid + queue in worst case

        rows, cols = len(grid), len(grid[0])
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

        visited = [[False] * cols for _ in range(rows)]
        que = deque()

        # Step 1: Enqueue all border land cells (multi-source)
        for row in range(rows):
            for col in range(cols):
                is_border = row == 0 or row == rows - 1 or col == 0 or col == cols - 1
                if is_border and grid[row][col] == 1:
                    visited[row][col] = True
                    que.append((row, col))

        # Step 2: BFS inward through connected land cells
        while que:
            i, j = que.popleft()

            for di, dj in directions:
                ni, nj = i + di, j + dj

                if 0 <= ni < rows and 0 <= nj < cols and not visited[ni][nj]:
                    if grid[ni][nj] == 1:  # only continue through land
                        visited[ni][nj] = True
                        que.append((ni, nj))

        # Step 3: Count land cells that were NEVER reached (true enclaves)
        count = 0
        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == 1 and not visited[row][col]:
                    count += 1

        return count
