# """
# This is the robot's control interface.
# You should not implement it, or speculate about its implementation
# """
# class Robot:
#    def move(self):
#        """
#        Returns true if the cell in front is open and robot moves into the cell.
#        Returns false if the cell in front is blocked and robot stays in the current cell.
#        :rtype bool
#        """
#
#    def turnLeft(self):
#        """
#        Robot will stay in the same cell after calling turnLeft/turnRight.
#        Each turn will be 90 degrees.
#        :rtype void
#        """
#
#    def turnRight(self):
#        """
#        Robot will stay in the same cell after calling turnLeft/turnRight.
#        Each turn will be 90 degrees.
#        :rtype void
#        """
#
#    def clean(self):
#        """
#        Clean the current cell.
#        :rtype void
#        """


class Solution:
    # Date Solved: 28 May 2026, Thursday
    # Solved previously as part of Weekly Premium on 9 May 2026, Saturday
    # Not in NC250 but related to Word Search (Blind 75)
    # In Namaste DSA course, Akshay Saini in Backtracking: Word Search (Blind 75) lecture, mentions to solve this as this is related to the Word Search problem.
    # Time: O(4*(M * N - O)) = O(M * N - O), Space: O(M * N - O)
    def cleanRoom(self, robot):
        visited = set()
        directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]

        def goBack():
            robot.turnRight()
            robot.turnRight()
            robot.move()
            robot.turnRight()
            robot.turnRight()

        def dfs(r, c, d):
            robot.clean()
            visited.add((r, c))

            for i in range(4):
                nextDir = (d + i) % 4
                nr, nc = r + directions[nextDir][0], c + directions[nextDir][1]

                if (nr, nc) not in visited and robot.move():
                    dfs(nr, nc, nextDir)
                    goBack()

                robot.turnRight()

        dfs(0, 0, 0)
