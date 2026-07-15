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
    # In NC All but Pro needed
    def employeeFreeTime(self, schedule: "[[Interval]]") -> "[Interval]":
        # Approach 1: Line Sweep (event-based)
        # Break each employee's intervals into OPEN (+1) and CLOSE (-1) events.
        # Sort all events by time. Track how many employees are busy right now (bal).
        # Whenever bal drops to 0, everyone is free -> mark the start of a gap.
        # The next time bal goes from 0 -> positive, that gap just ended -> record it.
        OPEN, CLOSE = 1, -1
        events = []

        for employee in schedule:
            for interval in employee:
                events.append((interval.start, OPEN))  # employee starts working
                events.append((interval.end, CLOSE))  # employee stops working

        events.sort()

        ans = []
        busy_count = 0
        gap_start = None

        for time, event_type in events:
            if busy_count == 0 and event_type == OPEN:
                # someone just started working after everyone was free. Free gap [gap_start, time) just ended
                if gap_start is not None and time > gap_start:
                    ans.append(Interval(gap_start, time))

            busy_count += event_type

            if busy_count == 0:
                # everyone just became free -> a new gap starts here
                gap_start = time

        return ans

        """
        # Approach 2: Sort and Merge
        # Nearly identical to LC 56 Merge Intervals with one extra step.
        # LC56: sort + merge overlapping intervals: return merged spans
        # LC759: sort + merge overlapping intervals: return the GAPS between merged spans
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
