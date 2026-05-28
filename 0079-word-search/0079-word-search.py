class Solution:
    # Date Solved: 28 May 2026, Thursday
    # Blind 75, (Word Search II is also Blind 75 but Hard level)
    # Classic Backtracking. This solution is hybrid and optimal created using codestorywithMIK, NeetCode and Namaste DSA
    # Time: O(M * N * 3^L) where M = rows, N = cols, L = length of word, Space: O(L)
    def exist(self, board: List[List[str]], word: str) -> bool:
        ROWS, COLS = len(board), len(board[0])

        if ROWS * COLS < len(word):
            return False

        def dfs(r, c, i):
            if i == len(word):
                return True
            if r < 0 or c < 0 or r >= ROWS or c >= COLS or board[r][c] != word[i]:
                return False

            board[r][c] = "#"
            res = (
                dfs(r + 1, c, i + 1)
                or dfs(r - 1, c, i + 1)
                or dfs(r, c + 1, i + 1)
                or dfs(r, c - 1, i + 1)
            )
            board[r][c] = word[i]

            return res

        for r in range(ROWS):
            for c in range(COLS):
                if dfs(r, c, 0):
                    return True
        return False
