class Solution:
    # Date Solved: 24 August 2026, Monday, POTD
    # Refer: codestorywithMIK
    # Time: O(n), Space: O(n)
    def stoneGameVIII(self, stones: List[int]) -> int:
        # Approach-1: Recursion + Memo
        # Time: O(n), Space: O(n)
        n = len(stones)
        prefixSum = list(accumulate(stones))
        t = {}

        def solve(i: int) -> int:
            if i == n - 1:
                return prefixSum[n - 1]

            if i in t:
                return t[i]

            take = prefixSum[i] - solve(i + 1)
            skip = solve(i + 1)

            t[i] = max(take, skip)
            return t[i]

        return solve(1)  # Alice turns first
        """
        # Approach-2: Bottom-up
        # Time: O(n), Space: O(n)
        n = len(stones)
        prefixSum = list(accumulate(stones))

        t = [0] * n
        t[n - 1] = prefixSum[n - 1]  # base case: solve(n-1)

        for i in range(n - 2, 0, -1):
            take = prefixSum[i] - t[i + 1]
            skip = t[i + 1]
            t[i] = max(take, skip)

        return t[1]  # == solve(1)
        """
