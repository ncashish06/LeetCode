class Solution:
    # Date Solved: 5 April 2026, Sunday, POTD
    # Refer: codestorywithMIK
    def judgeCircle(self, moves: str) -> bool:
        x, y = 0, 0
        for move in moves:
            if move == "U":
                y += 1
            elif move == "D":
                y -= 1
            elif move == "L":
                x -= 1
            elif move == "R":
                x += 1

        return x == y == 0
