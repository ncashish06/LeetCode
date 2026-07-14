MOD = 10**9 + 7


def gcd(a: int, b: int) -> int:
    while b:
        a, b = b, a % b
    return a


# Date Solved: 14 July 2026, Tuesday, POTD
# Refer: codestorywithMIK
class Solution:
    def subsequencePairCount(self, nums: List[int]) -> int:
        """
        # Approach-1: Recursion + Memoization
        # Time : O(n * M * M), M = max element
        # Space : O(n * M * M), M = max element
        n = len(nums)
        maxEl = max(nums)

        # t[i][first][second], -1 means "not computed yet"
        t = [[[-1] * (maxEl + 1) for _ in range(maxEl + 1)] for _ in range(n + 1)]

        def solve(i: int, first: int, second: int) -> int:
            if i == n:
                bothNonEmpty = first != 0 and second != 0
                gcdsMatch = first == second
                return 1 if (bothNonEmpty and gcdsMatch) else 0

            if t[i][first][second] != -1:
                return t[i][first][second]

            # Skip this index entirely
            skip = solve(i + 1, first, second)

            # Include this index in seq1
            take1 = solve(i + 1, gcd(first, nums[i]), second)

            # Include this index in seq2
            take2 = solve(i + 1, first, gcd(second, nums[i]))

            t[i][first][second] = (skip + take1 + take2) % MOD
            return t[i][first][second]

        return solve(0, 0, 0)
        """
        # Approach-2: Bottom Up (optimized with precomputed gcd table)
        # Time  : O(n * M * M), M = max element
        # Space : O(M * M)
        n = len(nums)
        maxEl = -1
        for x in nums:
            if x > maxEl:
                maxEl = x

        gcdTable = [[0] * (maxEl + 1) for _ in range(maxEl + 1)]
        for a in range(maxEl + 1):
            row = gcdTable[a]
            for b in range(a, maxEl + 1):
                g = gcd(a, b)
                row[b] = g
                gcdTable[b][a] = g

        # dp[first][second], representing layer i+1 initially (base case)
        dp = [[0] * (maxEl + 1) for _ in range(maxEl + 1)]
        for first in range(maxEl + 1):
            row = dp[first]
            for second in range(maxEl + 1):
                bothNonEmpty = first != 0 and second != 0
                gcdsMatch = first == second
                row[second] = 1 if (bothNonEmpty and gcdsMatch) else 0

        for i in range(n - 1, -1, -1):
            val = nums[i]
            gcdCol = gcdTable[val]  # gcdCol[x] == gcd(val, x)
            prev = dp  # dp for layer i+1
            curr = [[0] * (maxEl + 1) for _ in range(maxEl + 1)]

            for first in range(maxEl, -1, -1):
                g1 = gcdCol[first]  # gcd(first, val)
                row_first = prev[first]  # prev[first][*]  -> "skip"
                row_g1 = prev[g1]  # prev[gcd(first,val)][*] -> "take1"
                curr_row = curr[first]

                for second in range(maxEl, -1, -1):
                    skip = row_first[second]
                    take1 = row_g1[second]
                    take2 = row_first[gcdCol[second]]  # prev[first][gcd(second,val)]
                    curr_row[second] = (skip + take1 + take2) % MOD

            dp = curr

        return dp[0][0]
