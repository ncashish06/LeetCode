class Solution:
    # Date Solved: 15 July 2026, Wednesday
    # Blind 75
    # Refer: NC Ashish, solved on my own after practicing other "Intervals" problem.
    def canAttendMeetings(self, intervals: List[List[int]]) -> bool:
        if len(intervals) == 0:
            return True
        intervals.sort()
        prev_end = intervals[0][1]
        for i in range(1, len(intervals)):
            start, end = intervals[i][0], intervals[i][1]
            if start < prev_end:
                return False
            prev_end = end
        return True
