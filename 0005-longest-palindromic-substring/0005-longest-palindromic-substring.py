class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        if n == 0:
            return ""

        dp = [[False] * n for _ in range(n)]
        start, end = 0, 0

        for i in range(n):
            dp[i][i] = True
            if i < n - 1 and s[i] == s[i + 1]:
                dp[i][i + 1] = True
                start, end = i, i + 1

        for length in range(3, n + 1):
            for i in range(0, n - length + 1):
                j = i + length - 1
                if s[i] == s[j] and dp[i + 1][j - 1]:
                    dp[i][j] = True
                    start, end = i, j

        return s[start:end + 1]