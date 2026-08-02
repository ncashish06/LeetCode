class Solution:
    # Date Solved: 3 April 2026, Thursday, POTD
    # Refer: codestorywithMIK, memoization solution leads to "Memory Limit Exceeded"
    # Time: O(m × n), Space: O(m × n)
    def maximumAmount(self, coins: List[List[int]]) -> int:
        m, n = len(coins), len(coins[0])
        NEG_INF = float("-inf")

        # dp[i][j][k] = max coins arriving at (i, j) having used exactly k neutralizations
        dp = [[[NEG_INF] * 3 for _ in range(n)] for _ in range(m)]

        # Starting cell
        dp[0][0][0] = coins[0][0]
        if coins[0][0] < 0:
            dp[0][0][1] = 0  # neutralize the very first cell

        for i in range(m):
            for j in range(n):
                if i == 0 and j == 0:
                    continue

                for k in range(3):
                    best = NEG_INF

                    # Came from above
                    if i > 0 and dp[i - 1][j][k] != NEG_INF:
                        best = max(best, dp[i - 1][j][k] + coins[i][j])

                    # Came from the left
                    if j > 0 and dp[i][j - 1][k] != NEG_INF:
                        best = max(best, dp[i][j - 1][k] + coins[i][j])

                    # Neutralizing this cell (only helps if it's negative)
                    if coins[i][j] < 0 and k > 0:
                        if i > 0 and dp[i - 1][j][k - 1] != NEG_INF:
                            best = max(best, dp[i - 1][j][k - 1])  # + 0
                        if j > 0 and dp[i][j - 1][k - 1] != NEG_INF:
                            best = max(best, dp[i][j - 1][k - 1])  # + 0

                    dp[i][j][k] = best

        return max(dp[m - 1][n - 1])
