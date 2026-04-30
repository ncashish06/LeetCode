class Solution:
    def maxPathScore(self, grid: List[List[int]], k: int) -> int:
        m, n = len(grid), len(grid[0])

        # dp[r][c] will store a dictionary where:
        # key = cost spent, value = max score for that cost
        dp = [[{} for _ in range(n)] for _ in range(m)]

        # Base case: Starting cell (0, 0)
        start_val = grid[0][0]
        start_cost = 1 if start_val > 0 else 0
        if start_cost <= k:
            dp[0][0][start_cost] = start_val

        for r in range(m):
            for c in range(n):
                if r == 0 and c == 0:
                    continue

                curr_val = grid[r][c]
                cost_inc = 1 if curr_val > 0 else 0

                # Check neighbors: Top and Left
                for prev_r, prev_c in [(r - 1, c), (r, c - 1)]:
                    if 0 <= prev_r < m and 0 <= prev_c < n:
                        for prev_cost, prev_score in dp[prev_r][prev_c].items():
                            new_cost = prev_cost + cost_inc
                            if new_cost <= k:
                                new_score = prev_score + curr_val
                                # Update DP with the maximum score for this specific cost
                                dp[r][c][new_cost] = max(
                                    dp[r][c].get(new_cost, -1), new_score
                                )

        # Find the max score at the destination within cost k
        final_scores = dp[m - 1][n - 1].values()
        return max(final_scores) if final_scores else -1
