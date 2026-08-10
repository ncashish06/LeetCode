class Solution:
    # Date Solved: 10 August 2026, Monday, POTD
    # Refer: Claude
    # Game Strategy: Unlike Stone Game I/II/III, this isn't a score-maximizing
    # game -- it's a win/lose game. On your turn, you win if there EXISTS at
    # least one square move that leaves your opponent in a losing state.
    # So it's an OR over "opponent loses" rather than a max/min over scores.
    def winnerSquareGame(self, n: int) -> bool:
        """
        # Approach-1: Recursion + Memoization
        # Time: O(n * sqrt(n)), Space: O(n)
        t = [None] * (n + 1)

        def solve(stones: int) -> bool:
            if stones == 0:
                return False  # current player has no move -> loses

            if t[stones] is not None:
                return t[stones]

            result = False
            j = 1
            while j * j <= stones:
                # If opponent loses after we remove j*j stones, we win
                if not solve(stones - j * j):
                    result = True
                    break
                j += 1

            t[stones] = result
            return t[stones]

        return solve(n)
        """
        # Approach-2: Converting Approach-1 above to Bottom Up
        # Time: O(n * sqrt(n)), Space: O(n)
        t = [False] * (n + 1)
        # t[i] = True if the player to move WINS with i stones remaining

        for i in range(1, n + 1):
            j = 1
            while j * j <= i:
                if not t[i - j * j]:
                    t[i] = True
                    break
                j += 1

        return t[n]
