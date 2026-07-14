class Solution:
    # Date Solved: 14 July 2026, Tuesday
    # Blind 75
    # Refer: codestorywithMIK. NeetCode's video approach uses 2 pointers but is similar to this.
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        # Using Line Sweep
        # Time : O(n log n)
        # Space : O(n) to store events in dict

        events = defaultdict(int)

        for start, end in intervals:
            events[start] += 1
            events[end] -= 1

        result = 0
        count = 0

        for time in sorted(events):
            count += events[time]
            result = max(result, count)

        return result
