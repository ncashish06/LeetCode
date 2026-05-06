class Solution:
    # Date Solved: 5 May 2026, Tuesday
    # Part of NeetCode All problems
    # Similar to LC26, LC27, LC283
    def rotateTheBox(self, boxGrid: List[List[str]]) -> List[List[str]]:
        ROWS, COLS = len(boxGrid), len(boxGrid[0])

        res = [["."] * ROWS for _ in range(COLS)]

        for r in range(ROWS):
            i = COLS - 1
            for c in reversed(range(COLS)):
                if boxGrid[r][c] == "#":
                    res[i][ROWS - r - 1] = "#"
                    i -= 1
                elif boxGrid[r][c] == "*":
                    res[c][ROWS - r - 1] = "*"
                    i = c - 1

        return res
