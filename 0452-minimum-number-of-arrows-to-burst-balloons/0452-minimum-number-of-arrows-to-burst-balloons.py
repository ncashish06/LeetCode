class Solution:
    # Date Solved: 15 July 2026, Wednesday
    # Approach 1 same as one of the approaches for "LC. 435 Non-Overlapping Intervals" which is Blind 75.
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        """
        # Approach-1 ("Non Overlapping Intervals"), Sort on "End coordinate"
        # Refer: Github solution of codestorywithMIK
        # Time: O(nlogn), Space: O(1)
        points.sort(key=lambda p: p[1])

        count = 1
        prev_end = points[0][1]

        for i in range(1, len(points)):
            start = points[i][0]
            if start > prev_end:  # no overlap
                count += 1
                prev_end = points[i][1]
        return count
        """
        # Approach-2: Sort on "Start coordinate"
        # Time: O(nlogn), Space: O(1)
        # Refer: codestorywithMIK
        points.sort()

        prev = points[0]
        count = 1

        for i in range(1, len(points)):
            start, end = points[i][0], points[i][1]
            prev_start, prev_end = prev[0], prev[1]

            if start > prev_end:  # no overlap
                count += 1
                prev = points[i]
            else:
                # overlap
                prev[0] = max(prev_start, start)
                prev[1] = min(prev_end, end)

        return count
