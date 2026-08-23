class Solution:
    # Date Solved: 22 August 2026, Saturday, Weekly Premium W3
    # Refer: Claude
    # In NC all
    def numberOfPatterns(self, m: int, n: int) -> int:
        # jumps[i][j] = the dot that must already be visited to go straight from i to j
        jumps = [[0] * 10 for _ in range(10)]
        jumps[1][3] = jumps[3][1] = 2
        jumps[1][7] = jumps[7][1] = 4
        jumps[3][9] = jumps[9][3] = 6
        jumps[7][9] = jumps[9][7] = 8
        jumps[1][9] = jumps[9][1] = 5
        jumps[3][7] = jumps[7][3] = 5
        jumps[2][8] = jumps[8][2] = 5
        jumps[4][6] = jumps[6][4] = 5

        visited = [False] * 10

        def dfs(curr: int, length: int) -> int:
            if length > n:
                return 0

            count = 1 if length >= m else 0

            visited[curr] = True
            for nxt in range(1, 10):
                if not visited[nxt]:
                    mid = jumps[curr][nxt]
                    if mid == 0 or visited[mid]:
                        count += dfs(nxt, length + 1)
            visited[curr] = False

            return count

        total = 0
        # By symmetry: 1, 3, 7, 9 (corners) are equivalent
        total += dfs(1, 1) * 4
        # 2, 4, 6, 8 (edges) are equivalent
        total += dfs(2, 1) * 4
        # 5 (center) is unique
        total += dfs(5, 1)

        return total
