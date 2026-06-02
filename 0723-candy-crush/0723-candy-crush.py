class Solution:
    # Date Solved: 2 June 2026, Tuesday, Weekly Premium W1
    def candyCrush(self, board: List[List[int]]) -> List[List[int]]:
        m, n = len(board), len(board[0])

        while True:
            crush = set()

            # Find horizontal matches (3+)
            for r in range(m):
                for c in range(n - 2):
                    a, b, c2 = (
                        abs(board[r][c]),
                        abs(board[r][c + 1]),
                        abs(board[r][c + 2]),
                    )
                    if a != 0 and a == b == c2:
                        crush |= {(r, c), (r, c + 1), (r, c + 2)}

            # Find vertical matches (3+)
            for r in range(m - 2):
                for c in range(n):
                    a, b, c2 = (
                        abs(board[r][c]),
                        abs(board[r + 1][c]),
                        abs(board[r + 2][c]),
                    )
                    if a != 0 and a == b == c2:
                        crush |= {(r, c), (r + 1, c), (r + 2, c)}

            # No more crushes -> board is stable
            if not crush:
                break

            # Zero out crushed candies
            for r, c in crush:
                board[r][c] = 0

            # Gravity: drop candies down column by column
            for c in range(n):
                write = m - 1
                for r in range(m - 1, -1, -1):
                    if board[r][c] != 0:
                        board[write][c] = board[r][c]
                        if write != r:
                            board[r][c] = 0
                        write -= 1
                # Fill remaining top rows with 0
                for r in range(write, -1, -1):
                    board[r][c] = 0

        return board
