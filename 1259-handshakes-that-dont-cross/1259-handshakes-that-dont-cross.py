class Solution:
    # Date Solved: 15 June 2026, Monday, Weekly Premium W3
    # Refer: Claude
    # This problem is equivalent to counting the nth Catalan number, where n = numPeople / 2.
    def numberOfWays(self, numPeople: int) -> int:
        MOD = 10**9 + 7
        n = numPeople // 2

        # dp[i] = Catalan number C(i) = number of non-crossing handshake ways for 2i people
        dp = [0] * (n + 1)
        dp[0] = 1  # base case: 0 people, 1 way (do nothing)

        for i in range(1, n + 1):
            for j in range(i):
                # Person 1 pairs with person at position 2*(j+1)
                # Left group has 2j people → dp[j] ways
                # Right group has 2*(i-j-1) people → dp[i-j-1] ways
                dp[i] = (dp[i] + dp[j] * dp[i - j - 1]) % MOD

        return dp[n]
