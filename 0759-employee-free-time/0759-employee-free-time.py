"""
# Definition for an Interval.
class Interval:
    def __init__(self, start: int = None, end: int = None):
        self.start = start
        self.end = end
"""


class Solution:
    # Date Solved: 19 May 2026, Tuesday
    # Weekly Premium W1
    def employeeFreeTime(self, schedule: "[[Interval]]") -> "[Interval]":
        """
        Approach: Nearly identical to LC 56 Merge Intervals with one extra step.
        LC56: sort + merge overlapping intervals: return merged spans
        LC759: sort + merge overlapping intervals: return the GAPS between merged spans
        """
        all_intervals = []
        for employee in schedule:
            for interval in employee:
                all_intervals.append(interval)

        all_intervals.sort(key=lambda pair: pair.start)

        merged = [[all_intervals[0].start, all_intervals[0].end]]

        for interval in all_intervals:
            start, end = interval.start, interval.end
            lastEnd = merged[-1][1]

            if start <= lastEnd:
                merged[-1][1] = max(lastEnd, end)
            else:
                merged.append([start, end])

        free_time = []
        for i in range(1, len(merged)):
            free_time.append(Interval(merged[i - 1][1], merged[i][0]))

        return free_time

        """
        LC56. Merge Intervals Code
        intervals.sort(key=lambda pair: pair[0])
        output = [intervals[0]]

        for start, end in intervals:
            lastEnd = output[-1][1]

            if start <= lastEnd:
                output[-1][1] = max(lastEnd, end)
            else:
                output.append([start, end])
        return output
        """
