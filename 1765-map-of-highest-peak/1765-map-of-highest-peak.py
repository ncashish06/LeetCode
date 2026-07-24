class Solution:
    # Date Solved: 24 July 2026, Friday
    # Refer: NeetCode and codestorywithMIK. codestorywithMIK uses an inner while loop  to process the queue level by level, which is not needed as every new cell just inherits "parent height + 1" regardless of what "level" the BFS is on. We don't need to know how many nodes are in the level.
    # Not NC250 but related to Rotting Oranges (NC150)
    def highestPeak(self, isWater: List[List[int]]) -> List[List[int]]:
        # Approach: Multi-Source BFS
        # Time: O(m * n) - visit all cells once,
        # Space: O(m * n) - queue can contain all cells in worst case
        m = len(isWater)
        n = len(isWater[0])

        height = [[-1] * n for _ in range(m)]
        que = deque()

        # Initialize all water cells with height 0 and add to queue
        for i in range(m):
            for j in range(n):
                if isWater[i][j] == 1:
                    height[i][j] = 0
                    que.append((i, j))

        directions = [(0, 1), (0, -1), (-1, 0), (1, 0)]

        # Multi-Source BFS
        while que:
            i, j = que.popleft()

            for di, dj in directions:
                ni, nj = i + di, j + dj

                if 0 <= ni < m and 0 <= nj < n and height[ni][nj] == -1:
                    height[ni][nj] = height[i][j] + 1
                    que.append((ni, nj))

        return height
