class Solution:
    # Date Solved: 5 July 2026, Sunday, POTD
    # Refer: codestorywithMIK and Claude
    def pathsWithMaxScore(self, board: List[str]) -> List[int]:
        n = len(board)
        MOD = 10**9 + 7

        board = [list(row) for row in board]
        board[0][0] = "0"  # 'E' -> 0
        board[n - 1][n - 1] = "0"  # 'S' -> 0

        # t[i][j] = (best score, count of paths) to reach (0,0) from (i,j)...
        # here we go bottom-up from (0,0) which represents 'E' as base case
        t = [[(0, 0)] * n for _ in range(n)]
        t[0][0] = (0, 1)

        def is_valid(i, j):
            return 0 <= i < n and 0 <= j < n and board[i][j] != "X"

        for i in range(n):
            for j in range(n):
                if i == 0 and j == 0:
                    continue
                if board[i][j] == "X":
                    continue

                up_score = up_paths = 0
                left_score = left_paths = 0
                diag_score = diag_paths = 0
                ch = board[i][j]

                if is_valid(i - 1, j):
                    score, paths = t[i - 1][j]
                    up_score, up_paths = score, paths
                    if up_paths > 0:
                        up_score += int(ch)

                if is_valid(i, j - 1):
                    score, paths = t[i][j - 1]
                    left_score, left_paths = score, paths
                    if left_paths > 0:
                        left_score += int(ch)

                if is_valid(i - 1, j - 1):
                    score, paths = t[i - 1][j - 1]
                    diag_score, diag_paths = score, paths
                    if diag_paths > 0:
                        diag_score += int(ch)

                if up_score == left_score == diag_score:
                    best_score = up_score
                    best_paths = up_paths + left_paths + diag_paths
                elif up_score == left_score:
                    best_score = up_score
                    best_paths = up_paths + left_paths
                    if diag_score > best_score or (
                        diag_score == best_score and diag_paths > best_paths
                    ):
                        best_score, best_paths = diag_score, diag_paths
                elif left_score == diag_score:
                    best_score = left_score
                    best_paths = left_paths + diag_paths
                    if up_score > best_score or (
                        up_score == best_score and up_paths > best_paths
                    ):
                        best_score, best_paths = up_score, up_paths
                else:
                    best_score, best_paths = up_score, up_paths
                    if left_score > best_score or (
                        left_score == best_score and left_paths > best_paths
                    ):
                        best_score, best_paths = left_score, left_paths
                    if diag_score > best_score or (
                        diag_score == best_score and diag_paths > best_paths
                    ):
                        best_score, best_paths = diag_score, diag_paths

                t[i][j] = (best_score, best_paths % MOD)

        return [t[n - 1][n - 1][0], t[n - 1][n - 1][1]]
