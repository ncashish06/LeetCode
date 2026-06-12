class Solution:
    # Date Solved: 12 June 2026, Friday
    # Blind 75
    # Refer: codestorywithMIK
    # Copy paste same solution as  in LC. 463 Island Perimeter with some changes
    def numIslands(self, grid: List[List[str]]) -> int:
        # Approach 1: DFS
        # Time: O(m*n), Space: O(m*n) recursion stack
        rows = len(grid)
        cols = len(grid[0])
        islands = 0

        def dfs(row, col):
            if (
                row < 0
                or row >= rows
                or col < 0
                or col >= cols
                or grid[row][col] != "1"
            ):
                return

            grid[row][col] = "$"  # mark visited

            dfs(row + 1, col)
            dfs(row - 1, col)
            dfs(row, col + 1)
            dfs(row, col - 1)

        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == "1":
                    dfs(row, col)
                    islands += 1

        return islands
