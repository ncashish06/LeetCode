class Solution:
    # Date Solved: 6 July 2026, Monday, POTD
    # Refer: codestorywithMIK. Also, in NC All with video explanation.
    # Good "Intervals" topic question for practice which will help with other "Intervals" Blind 75, NC150 problems.
    def removeCoveredIntervals(self, intervals: List[List[int]]) -> int:
        """
        # Approach 1: Using O(n) space and sorting. Time : O(nlogn), Space : O(n)
        result = []
        n = len(intervals)
        # sort by start ascending; on tie, end descending
        intervals.sort(key=lambda x: (x[0], -x[1]))
        result.append(intervals[0])
        for i in range(1, n):
            if result[-1][0] <= intervals[i][0] and result[-1][1] >= intervals[i][1]:
                continue
            result.append(intervals[i])
        return len(result)

        # Approach 2: Using O(n) space and sorting + Simplified condition check. Time : O(nlogn), Space : O(n)
        result = []
        n = len(intervals)
        intervals.sort(key=lambda x: (x[0], -x[1]))
        result.append(intervals[0])
        for i in range(1, n):
            # Simplified, As result[-1][0] <= intervals[i][0] is always true and is redundant (due to sorting)
            if result[-1][1] >= intervals[i][1]:
                continue
            result.append(intervals[i])
        return len(result)
        """
        # Approach 3: Using constant space and sorting. Time : O(nlogn), Space : O(1)
        n = len(intervals)
        intervals.sort(key=lambda x: (x[0], -x[1]))
        last_interval_ka_end = intervals[0][1]  # last_interval_ka_end, ka = hindi. Lol!
        count = 1
        for i in range(1, n):
            if last_interval_ka_end >= intervals[i][1]:
                continue
            last_interval_ka_end = intervals[i][1]
            count += 1
        return count
