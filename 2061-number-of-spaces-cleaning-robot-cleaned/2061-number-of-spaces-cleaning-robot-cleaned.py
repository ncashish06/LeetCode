class Solution:
    # Date Solved: 15 May 2026, Friday
    # Weekly Premium April 2026 - Week 3
    def numberOfCleanRooms(self, room: List[List[int]]) -> int:
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]

        rows, cols = len(room), len(room[0])
        cleaned = set()
        visited = set()

        row, col, direction = 0, 0, 0  # start at top-left, facing right

        while (row, col, direction) not in visited:
            visited.add((row, col, direction))
            cleaned.add((row, col))

            # Try to move forward
            next_row, next_col = row + directions[direction][0], col + directions[direction][1]

            if (
                0 <= next_row < rows
                and 0 <= next_col < cols
                and room[next_row][next_col] == 0
            ):
                row, col = next_row, next_col  # Move forward
            else:
                direction = (direction + 1) % 4  # Hit wall or object — turn 90° clockwise

        return len(cleaned)
