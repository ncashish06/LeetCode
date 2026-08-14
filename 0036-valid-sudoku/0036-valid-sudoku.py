# Date Solved: 14 August 2026, Friday
# NC150
# Refer: codestorywithMIK
class Solution:
    """
    # Approach-1: Naive and simplest using 3 iterations of the sudoku
    def validSub(self, board, start_row, end_row, start_col, end_col):
        seen = set()
        for row in range(start_row, end_row + 1):
            for col in range(start_col, end_col + 1):
                ch = board[row][col]
                if ch == ".":
                    continue
                if ch in seen:
                    return False
                seen.add(ch)
        return True

    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # validate rows
        for row in range(9):
            seen = set()
            for col in range(9):
                ch = board[row][col]
                if ch == ".":
                    continue
                if ch in seen:
                    return False
                seen.add(ch)

        # validate columns
        for col in range(9):
            seen = set()
            for row in range(9):
                ch = board[row][col]
                if ch == ".":
                    continue
                if ch in seen:
                    return False
                seen.add(ch)

        # validate ech 3*3 box
        for start_row in range(0, 9, 3):
            end_row = start_row + 2
            for start_col in range(0, 9, 3):
                end_col = start_col + 2
                if not self.validSub(board, start_row, end_row, start_col, end_col):
                    return False

        return True
    """

    # Approach-2: One iteration using hashmap and indexing boxes
    def isValidSudoku(self, board) -> bool:
        seen = set()

        for i in range(9):
            for j in range(9):
                if board[i][j] == ".":
                    continue
                # Adding a string to compare, can be any string concatenation.
                row = board[i][j] + "_row_" + str(i)
                col = board[i][j] + "_col_" + str(j)
                box = board[i][j] + "_box_" + str(i // 3) + "_" + str(j // 3)
                if row in seen or col in seen or box in seen:
                    return False
                seen.add(row)
                seen.add(col)
                seen.add(box)

        return True
