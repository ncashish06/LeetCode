class Solution:
    # Date Solved: 3 August 2026, Monday, POTD
    # Refer: codestorywithMIK
    # NC250
    # Game Strategy: When it is your turn, do your best and choose maximum. Since opponent also plays optimally, expect the worst from result after opponent's turn. So it is alternating max->min->max->min... structure of the recursion, i.e., classic minimax: maximize on your turn, minimize (from your perspective) on the opponent's turn
    def stoneGameIII(self, stoneValue: List[int]) -> str:
        """
        # Approach-1: Using simple recursion + memoization
        # Time: O(n), Space: O(n)
        n = len(stoneValue)
        t = [None] * (n + 1)

        def solve(i: int) -> int:
            if i == n:
                return 0

            if t[i] is not None:
                return t[i]

            result = stoneValue[i] - solve(i + 1)

            if i + 1 < n:
                result = max(result, stoneValue[i] + stoneValue[i + 1] - solve(i + 2))

            if i + 2 < n:
                result = max(
                    result,
                    stoneValue[i]
                    + stoneValue[i + 1]
                    + stoneValue[i + 2]
                    - solve(i + 3),
                )

            t[i] = result
            return t[i]

        diff = solve(0)

        if diff < 0:
            return "Bob"
        elif diff > 0:
            return "Alice"
        return "Tie"
        """
        # Approach-2: Converting approach-1 to Bottom Up
        # Time: O(n), Space: O(n)
        n = len(stoneValue)

        t = [0] * (n + 1)
        # t[i] = Alice - Bob

        for i in range(n - 1, -1, -1):
            t[i] = stoneValue[i] - t[i + 1]

            if i + 2 <= n:
                t[i] = max(t[i], stoneValue[i] + stoneValue[i + 1] - t[i + 2])

            if i + 3 <= n:
                t[i] = max(
                    t[i],
                    stoneValue[i] + stoneValue[i + 1] + stoneValue[i + 2] - t[i + 3],
                )

        diff = t[0]

        if diff < 0:
            return "Bob"
        elif diff > 0:
            return "Alice"
        return "Tie"
        """
        # Approach-3: Converting Approach-2 above to constant space
        # Time: O(n), Space: O(1)
        n = len(stoneValue)

        a = 0
        b = 0
        c = 0

        for i in range(n - 1, -1, -1):
            result = float("-inf")

            result = max(result, stoneValue[i] - b)

            if i + 2 <= n:
                result = max(result, stoneValue[i] + stoneValue[i + 1] - b)

            if i + 3 <= n:
                result = max(
                    result, stoneValue[i] + stoneValue[i + 1] + stoneValue[i + 2] - c
                )

            c = b
            b = a
            a = result

        diff = a

        if diff < 0:
            return "Bob"
        elif diff > 0:
            return "Alice"
        return "Tie"
        """
