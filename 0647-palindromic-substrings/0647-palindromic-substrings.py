class Solution:
    def countSubstrings(self, s: str) -> int:
        n = len(s)
        dp = [[None] * n for _ in range(n)]
        ans = 0
        for i in range(n):
            dp[i][i] = True
            ans += 1
            if i < n - 1 and s[i] == s[i + 1]:
                dp[i][i + 1] = True
                ans += 1

        for length in range(3, n + 1):
            for i in range(0, n - length + 1):
                j = i + length - 1
                # first and last characters are same and inner substring is palindrome, then these characters also form palindrome
                if s[i] == s[j] and dp[i + 1][j - 1]:
                    dp[i][j] = True
                    ans += 1
        return ans
