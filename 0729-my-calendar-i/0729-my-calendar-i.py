# Date Solved: 13 July 2026, Monday
# In NC all under "Intervals" topic
# Refer: NeetCode. codestorywithMIK uses built-in data structure like SortedList
"""
# No line sweep here as in "My Calendar II" because re-sorting all events on every call just to detect a simple pairwise overlap, makes it O(n log n) per call, O(n^2 log n) overall. That's strictly worse than brute force here. Line sweep is useful in Calendar II because you need to track how many bookings overlap at a point (to catch triples); but here you only need a yes/no on any overlap, so the sweep's bookkeeping is wasted effort.
"""

"""
# Approach 1: Brute force
# Time: O(n) per booking, O(n^2) overall
class MyCalendar:
    def __init__(self):
        self.bookings = []

    def book(self, startTime: int, endTime: int) -> bool:
        for start, end in self.bookings:
            if startTime < end and start < endTime:
                return False

        self.bookings.append((startTime, endTime))
        return True
"""


# Approach 2: Binary Search Tree
# Time: O(log n) average per booking (tree stays roughly balanced with random inputs),
# O(n) worst case if bookings arrive in sorted/monotonic order
# Space: O(n) for storing n booked events as tree nodes
class Node:
    def __init__(self, start, end):
        self.start = start
        self.end = end
        self.left = None  # points to subtree of events before this one
        self.right = None  # points to subtree of events after this one

    def insert(self, start, end):
        # New event ends before (or exactly when) this node starts -> no overlap here,
        # recurse into the left subtree (earlier events).
        if end <= self.start:
            if self.left is None:
                self.left = Node(start, end)
                return True
            return self.left.insert(start, end)

        # New event starts after (or exactly when) this node ends -> no overlap here,
        # recurse into the right subtree (later events).
        elif start >= self.end:
            if self.right is None:
                self.right = Node(start, end)
                return True
            return self.right.insert(start, end)

        # Otherwise the intervals must overlap -> double booking, reject it.
        else:
            return False  # overlap


class MyCalendar:
    def __init__(self):
        self.root = None

    def book(self, startTime: int, endTime: int) -> bool:
        # First event becomes the root
        if self.root is None:
            self.root = Node(startTime, endTime)
            return True
        return self.root.insert(startTime, endTime)


# Your MyCalendar object will be instantiated and called as such:
# obj = MyCalendar()
# param_1 = obj.book(startTime,endTime)
