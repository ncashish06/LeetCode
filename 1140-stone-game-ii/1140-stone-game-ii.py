class Solution:
    # Date Solved: 9 August 2026, Sunday, POTD
    # Refer: codestorywithMIK
    # NC250
    # Game Strategy: When it is your turn, do your best and choose maximum. Since opponent also plays optimally, expect the worst from result after opponent's turn. So it is alternating max->min->max->min... structure of the recursion, i.e., classic minimax: maximize on your turn, minimize (from your perspective) on the opponent's turn
    # Time: O(n^3), Space: O(n^3)
    def stoneGameII(self, piles: List[int]) -> int:
        n = len(piles)

        # t[person][i][M] -> memo table
        # person = 1 -> Alice, person = 0 -> Bob
        t = [[[-1] * (n + 1) for _ in range(n + 1)] for _ in range(2)]

        def solveForAlice(person: int, i: int, M: int) -> int:
            if i >= n:
                return 0

            if t[person][i][M] != -1:
                return t[person][i][M]

            result = -1 if person == 1 else float("inf")

            stones = 0

            # To be within array limits: min(2 * M, n - i)
            for x in range(1, min(2 * M, n - i) + 1):

                stones += piles[i + x - 1]

                if person == 1:  # Alice
                    result = max(result, stones + solveForAlice(0, i + x, max(M, x)))
                else:  # Bob
                    result = min(result, solveForAlice(1, i + x, max(M, x)))

            t[person][i][M] = result
            return result

        return solveForAlice(1, 0, 1)
