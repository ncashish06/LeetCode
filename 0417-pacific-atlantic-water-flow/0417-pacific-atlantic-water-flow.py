class Solution:
    # Date Solved: 25 July 2026, Saturday
    # Blind 75
    # Refer: NC Ashish. codestorywithMIK and NeetCode do DFS from all border cells.
    # NeetCode and LeetCode editorials have this Multi-Source BFS approach.
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        # Approach: Multi-Source BFS from ocean's border. Simple BFS from all border cells would also lead to the same asymptotic complexity as visited cells are not processed again.
        # Time: O(rows * cols) - each cell visited at most once per ocean BFS
        # Space: O(rows * cols) - visited sets + queue in worst case

        rows, cols = len(heights), len(heights[0])
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

        def multiSourceBFS(starts):
            visited = [[False] * cols for _ in range(rows)]
            que = deque()

            # Enqueue with all border cells at once (multi-source)
            for r, c in starts:
                visited[r][c] = True
                que.append((r, c))

            while que:
                i, j = que.popleft()

                for di, dj in directions:
                    ni, nj = i + di, j + dj

                    if 0 <= ni < rows and 0 <= nj < cols and not visited[ni][nj]:
                        # Reverse-flow condition: neighbor must be >= current
                        # (water at neighbor can flow DOWN into current cell,
                        # which we already know reaches the ocean)
                        if heights[ni][nj] >= heights[i][j]:
                            visited[ni][nj] = True
                            que.append((ni, nj))

            return visited

        # Pacific Ocean touches the top row and the left column
        pacific_starts = []

        # Add every cell in the top row
        for col in range(cols):
            pacific_starts.append((0, col))

        # Add every cell in the left column
        for row in range(rows):
            pacific_starts.append((row, 0))

        # Atlantic Ocean touches the bottom row and the right column
        atlantic_starts = []

        # Add every cell in the bottom row
        for col in range(cols):
            atlantic_starts.append((rows - 1, col))

        # Add every cell in the right column
        for row in range(rows):
            atlantic_starts.append((row, cols - 1))

        pacific_reachable = multiSourceBFS(pacific_starts)
        atlantic_reachable = multiSourceBFS(atlantic_starts)

        # Cell qualifies only if it can reach BOTH oceans
        result = []
        for i in range(rows):
            for j in range(cols):
                if pacific_reachable[i][j] and atlantic_reachable[i][j]:
                    result.append([i, j])

        return result
