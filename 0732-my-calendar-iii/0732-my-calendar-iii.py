# Date Solved: 14 July 2026, Tuesday
# Refer: codestorywithMIK (Line Sweep technique). Similar to My Calendar II
# Not in NC All
# Approach (Using Line Sweep)
# Time : O(n log n), where n = number of events, Space : O(n) to store events in dict
class MyCalendarThree:

    def __init__(self):
        self.events = defaultdict(int)

    def book(self, startTime: int, endTime: int) -> int:
        self.events[startTime] += 1
        self.events[endTime] -= 1

        count = 0
        maxCount = 0

        for time in sorted(self.events):
            count += self.events[time]
            maxCount = max(maxCount, count)

        return maxCount


# Your MyCalendarThree object will be instantiated and called as such:
# obj = MyCalendarThree()
# param_1 = obj.book(startTime,endTime)
