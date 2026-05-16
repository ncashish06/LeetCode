class Solution:
    # Date Solved: 15 May 2026, Friday
    # Weekly Premium April 2026 - Week 3
    # Don't assume all 0's would be cleaned
    # Code very similar to LC.54 Spiral Matrix (Blind 75)
    def numberOfCleanRooms(self, room: List[List[int]]) -> int:
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]

        rows, cols = len(room), len(room[0])
        visited = set()
        cleaned = set() # As there will be multiple entries for each cell in the visited set, determining the number of cleaned cells may be challenging. Therefore, we will also maintain a set called cleaned, which solely stores the cell coordinates of each cleaned cell.

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
