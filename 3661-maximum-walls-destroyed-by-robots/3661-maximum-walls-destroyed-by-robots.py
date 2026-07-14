class Solution:
    # Date Solved: 3 April 2026, Friday, POTD
    # Refer: codestorywithMIK
    def maxWalls(self, robots: List[int], distance: List[int], walls: List[int]) -> int:
        n = len(robots)
        roboDist = sorted(zip(robots, distance))
        walls = sorted(walls)

        def countWalls(l: int, r: int) -> int:
            left = bisect_left(walls, l)
            right = bisect_right(walls, r)
            return right - left

        # Prepare reachable [L, R] range for each robot
        range_ = [None] * n
        for i in range(n):
            pos, d = roboDist[i]
            leftLimit = 1 if i == 0 else roboDist[i - 1][0] + 1
            rightLimit = 10**9 if i == n - 1 else roboDist[i + 1][0] - 1
            range_[i] = (max(pos - d, leftLimit), min(pos + d, rightLimit))

        # Memo table, t[i][prevDir], -1 means "not computed yet"
        t = [[-1, -1] for _ in range(n + 1)]

        def solve(i: int, prevDir: int) -> int:
            if i == n:
                return 0

            if t[i][prevDir] != -1:
                return t[i][prevDir]

            leftStart = range_[i][0]
            if prevDir == 1:
                leftStart = max(leftStart, range_[i - 1][1] + 1)

            pos = roboDist[i][0]
            leftTake = countWalls(leftStart, pos) + solve(i + 1, 0)
            rightTake = countWalls(pos, range_[i][1]) + solve(i + 1, 1)

            t[i][prevDir] = max(leftTake, rightTake)
            return t[i][prevDir]

        return solve(0, 0)
