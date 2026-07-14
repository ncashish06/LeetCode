class Solution:
    # Date Solved: 15 July 2026, Wednesday
    # NC250
    # Refer: codestorywithMIK (Line Sweep and Difference Array) and NeetCode (Min Heap and Difference Array). Namaste DSA gives the Difference Array approach
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        # Approach-1 (Using Line Sweep by codestorywithMIK)
        # Time: O(n log n)
        # Space: O(n) to store events in dict
        events = defaultdict(int)

        for count, start, end in trips:
            events[start] += count
            events[end] -= count

        passCount = 0

        for time in sorted(events):
            passCount += events[time]

            if passCount > capacity:
                return False

        return True
        """
        # Approach-2 (Using Min-Heap / Sorted by Start Time by NeetCode)
        # Time: O(n*logn) sorting trips + heap push/pop operations
        # Space: O(n) to store the heap

        trips.sort(key=lambda t: t[1])  # Sort trips by start location

        minHeap = []  # pair of [end, numPassengers]
        curPass = 0

        for numPass, start, end in trips:
            # Before picking up new passengers, drop off anyone whose trip has already ended by (or at) the current start point.
            # minHeap[0][0] is the earliest "end" among active trips.
            while minHeap and minHeap[0][0] <= start:
                curPass -= heapq.heappop(minHeap)[1]

            curPass += numPass
            if curPass > capacity:
                return False

            # Push this trip's [end, numPassengers] onto the heap,
            # so we know when to drop these passengers off later
            heapq.heappush(minHeap, [end, numPass])

        return True
        
        # Approach-3 (Using Difference Array Technique)
        # Time: O(n)
        # Space : O(1001) ~= O(1)
        diff = [0] * 1001

        for count, start, end in trips:
            diff[start] += count
            diff[end] -= count

        cumSum = 0

        for i in range(1001):
            cumSum += diff[i]

            if cumSum > capacity:
                return False

        return True
        """
