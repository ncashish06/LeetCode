class Robot:
    # Date Solved: 6 April 2026, Monday
    def __init__(self, width: int, height: int):
        self.w = width
        self.h = height
        # Imagine the boundary of the grid is a piece of string. If you "unroll" it, the robot is just moving along a straight line. When it reaches the end, it wraps back to the beginning.
        # Total unique steps around the boundary
        # Imagine a 3x3 grid. If you just add the lengths of the four sides, you get 3 + 3 + 3 + 3 = 12
        # However, the actual cells on the edge are only 8 unique cells. Because every corner belongs to two sides at once
        # Total unique cells = (Width - 1) + (Height - 1) + (Width - 1) + (Height - 1) = 2x(Width+Height)-2
        self.perimeter = (width + height - 2) * 2
        self.current_pos = 0
        self.has_moved = False

        # Sequence: Bottom Edge -> Right Edge -> Top Edge -> Left Edge
        # Precomputation: We precalculate every single coordinate on the boundary and the direction the robot usually faces there. This makes getPos and getDir instant (O(1)).
        self.cells = []

        # Think about the given example scenario
        # Bottom (East)
        # We take all x from 0 to 5. This includes both the bottom-left and bottom-right corners.
        for x in range(width): 
            self.cells.append([x, 0, "East"])

        # Right (North) - skip (width-1, 0)
        # We start at y=1 instead of 0, because (5, 0) was already "claimed" by the bottom edge loop above
        for y in range(1, height):
            self.cells.append([width - 1, y, "North"]) # width-1 because 0-based indexing (0 to 5 for width 6).

        # Top (West) - skip (width-1, height-1)
        # We start at x = width - 2 (which is 4), because (5, 2) was already "claimed" by the right edge loop.
        for x in range(width - 2, -1, -1):
            self.cells.append([x, height - 1, "West"]) # height-1 because 0-based indexing (0 to 2 for height 3).

        # Left (South) - skip (0, height-1) and (0, 0)
        # We stop before 0, because (0, 0) was the very first cell we added!
        for y in range(height - 2, 0, -1):
            self.cells.append([0, y, "South"])

    def step(self, num: int) -> None:
        self.has_moved = True
        # If the robot is told to move 2,000 steps on a perimeter of 14, we only care about 2000%14.
        # This turns an O(N) simulation into an O(1) math problem.
        self.current_pos = (self.current_pos + num) % self.perimeter

    def getPos(self) -> List[int]:
        x, y, _ = self.cells[self.current_pos]
        return [x, y]

    def getDir(self) -> str:
        # Special Case: If at (0,0) after moving a full lap, it must face South (as it just "turned" from the left edge)
        if self.has_moved and self.current_pos == 0:
            return "South"
        return self.cells[self.current_pos][2]


# Your Robot object will be instantiated and called as such:
# obj = Robot(width, height)
# obj.step(num)
# param_2 = obj.getPos()
# param_3 = obj.getDir()
