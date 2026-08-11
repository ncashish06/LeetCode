class Solution:
    # Date Solved: 2 August 2026, Sunday, POTD
    # Refer: codestorywithMIK
    # NC250
    # Game Strategy: When it is your turn, do your best and choose maximum. Since opponent also plays optimally, expect the worst from result after opponent's turn. So it is alternating max->min->max->min... structure of the recursion, i.e., classic minimax: maximize on your turn, minimize (from your perspective) on the opponent's turn
    def stoneGame(self, piles: List[int]) -> bool:
        # Approach 1: Recursion+Memo which is the standard optimal Game Strategy concept
        # Time: O(n^2), Space: O(n^2)
        n = len(piles)
        t = {}

        def solve(i: int, j: int) -> int:
            if i > j:
                return 0

            if (i, j) in t:
                return t[(i, j)]

            # That's how optimal game strategy works. Expect your opponent to be playing optimally
            # - When it's your turn, do your best
            # - When it's your opponent's turn, expect the worst (that's why min() is taken below)
            # Note: 2 lines below tell what Alice has picked now and what is available to her after Bob's turn based on what Bob picks, i or j.
            choose_i = piles[i] + min(solve(i + 2, j), solve(i + 1, j - 1))
            choose_j = piles[j] + min(solve(i, j - 2), solve(i + 1, j - 1))

            t[(i, j)] = max(choose_i, choose_j)
            return t[(i, j)]

        total = sum(piles)
        alice_score = solve(0, n - 1)

        return alice_score > total // 2
        """
        # Approach 2: Since there's an even number of piles and no ties, the first player (Alice) can always force a win using a parity strategy (always take piles at even indices or always odd, whichever sums higher), so you can always returns True
        # Time: O(1), Space: O(1)
        return True
        """
