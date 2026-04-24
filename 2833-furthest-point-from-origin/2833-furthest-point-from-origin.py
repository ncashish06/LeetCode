class Solution:
    # Date Solved: 23 April 2026, Thursday
    def furthestDistanceFromOrigin(self, moves: str) -> int:
        l, r, unknown = 0, 0, 0
        for i in range(len(moves)):
            if moves[i] == "L":
                l += 1
            elif moves[i] == "R":
                r += 1
            else:
                unknown += 1

        max_distance = max(l, r) - min(l, r) + unknown
        return max_distance
