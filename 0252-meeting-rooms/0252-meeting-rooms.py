class Solution:
    # Date Solved: 15 July 2026, Wednesday
    # Blind 75
    # Refer: NC Ashish, solved on my own after practicing other "Intervals" problem.
    # No codestorywithMIK and NeetCode's approach similar to mine.
    def canAttendMeetings(self, intervals: List[List[int]]) -> bool:
        # Time: O(nlogn), Space: O(1) ignoring extra space used by sorting
        if len(intervals) == 0:
            return True
        intervals.sort(key=lambda x: x[0])
        prev_end = intervals[0][1]
        for i in range(1, len(intervals)):
            start, end = intervals[i][0], intervals[i][1]
            if start < prev_end:  # Golden rule to check overlap
                return False
            prev_end = end
        return True
