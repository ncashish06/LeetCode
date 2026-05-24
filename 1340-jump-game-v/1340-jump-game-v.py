class Solution:
    # Date Solved: 24 May 2026, Sunday
    # POTD (Not in Neetcode 250)
    # Refer: codestorywithMIK
    def maxJumps(self, arr: List[int], d: int) -> int:
        # Approach 1: Recursion + Memoization
        # Time: O(n*d), Space: O(n)
        n = len(arr)
        memo = [-1] * n

        def solve(i):
            if memo[i] != -1:
                return memo[i]

            result = 1  # count current index

            # move left
            for j in range(i - 1, max(-1, i - d - 1), -1):
                if arr[j] >= arr[i]:
                    break
                result = max(result, 1 + solve(j))

            # move right
            for j in range(i + 1, min(n, i + d + 1)):
                if arr[j] >= arr[i]:
                    break
                result = max(result, 1 + solve(j))

            memo[i] = result
            return result

        return max(solve(i) for i in range(n))
        """
        # Approach 2: Bottom-Up DP using Sorting
        # Time: O(n*d), Space: O(n)
        n = len(arr)
        dp = [1] * n

        # Sort indices by their array values (process smaller values first)
        sorted_indices = sorted(range(n), key=lambda i: arr[i])

        for i in sorted_indices:
            # move left
            for j in range(i - 1, max(-1, i - d - 1), -1):
                if arr[j] >= arr[i]:
                    break
                dp[i] = max(dp[i], 1 + dp[j])

            # move right
            for j in range(i + 1, min(n, i + d + 1)):
                if arr[j] >= arr[i]:
                    break
                dp[i] = max(dp[i], 1 + dp[j])

        return max(dp)
        """
