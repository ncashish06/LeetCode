class Solution:
    # Date Solved: 20 June 2026, Saturday, POTD
    def maxBuilding(self, n: int, restrictions: List[List[int]]) -> int:
        height_limits = list(restrictions)
        height_limits.append([1, 0])

        # Building n's height can't exceed n - 1 anyway (since we start at 0 and
        # climb by at most 1 per step), so maxHeight = n is a safe.
        # Only add it if building n isn't already explicitly restricted.
        if not any(rid == n for rid, _ in restrictions):
            height_limits.append([n, n])

        # Sort by building id so we can scan left to right.
        height_limits.sort()

        # Forward pass — propagate constraints left to right.
        # A building's max height can't exceed (previous checkpoint's
        # height) + (distance to it), since height changes by at most 1
        # per building.
        for i in range(1, len(height_limits)):
            prev_id, prev_h = height_limits[i - 1]
            curr_id, curr_h = height_limits[i]
            distance = curr_id - prev_id
            height_limits[i][1] = min(curr_h, prev_h + distance)

        # Backward pass — propagate constraints right to left.
        # Same logic, mirrored: bound each height by the next checkpoint's
        # height + distance to it.
        for i in range(len(height_limits) - 2, -1, -1):
            next_id, next_h = height_limits[i + 1]
            curr_id, curr_h = height_limits[i]
            distance = next_id - curr_id
            height_limits[i][1] = min(curr_h, next_h + distance)

        max_height = 0
        for i in range(1, len(height_limits)):
            id1, h1 = height_limits[i - 1]
            id2, h2 = height_limits[i]
            distance = id2 - id1
            peak = (h1 + h2 + distance) // 2
            max_height = max(max_height, peak)

        return max_height
