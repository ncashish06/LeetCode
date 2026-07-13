# Date Solved: 13 July 2026, Monday
# In NC all under "Intervals" topic
# Refer: NeetCode or codestorywithMIK


# Unlike My Calendar I, there is no need of Binary Search Tree(BST) here.
# Time Complexity: O(n) per booking (scan overlaps + bookings), O(n^2) overall
# Space Complexity: O(n) for bookings and overlaps lists
class MyCalendarTwo:
    def __init__(self):
        self.bookings = []  # all successfully booked events
        self.overlaps = []  # double-booked zones

    def book(self, startTime: int, endTime: int) -> bool:
        # If the new event intersects any existing double-booked region,
        # booking it would create a triple booking -> reject.
        for s, e in self.overlaps:
            if startTime < e and s < endTime:
                return False

        # Otherwise it's safe. Find any overlap this new event creates
        # with existing single bookings -> those become new double-booked zones.
        for s, e in self.bookings:
            if startTime < e and s < endTime:
                self.overlaps.append((max(startTime, s), min(endTime, e)))

        # Finally, record this event as a booking.
        self.bookings.append((startTime, endTime))
        return True


# Your MyCalendarTwo object will be instantiated and called as such:
# obj = MyCalendarTwo()
# param_1 = obj.book(startTime,endTime)
