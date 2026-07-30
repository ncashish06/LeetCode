class Solution:
    # Date Solved: 30 July 2026, Thursday
    # codestorywithMIK says asked in Juspay OA.
    # Refer: codestorywithMIK
    def minCost(self, startPos: List[int], homePos: List[int], rowCosts: List[int], colCosts: List[int]) -> int:
        r1, c1 = startPos[0], startPos[1]
        r2, c2 = homePos[0], homePos[1]

        res = 0

        # Move in rows
        if r2 >= r1:
            # moving DOWN
            for r in range(r1 + 1, r2 + 1):
                res += rowCosts[r]
        else:
            # moving UP
            for r in range(r1 - 1, r2 - 1, -1):
                res += rowCosts[r]

        # Move in columns
        if c2 >= c1:
            # moving RIGHT
            for c in range(c1 + 1, c2 + 1):
                res += colCosts[c]
        else:
            # moving LEFT
            for c in range(c1 - 1, c2 - 1, -1):
                res += colCosts[c]

        return res
