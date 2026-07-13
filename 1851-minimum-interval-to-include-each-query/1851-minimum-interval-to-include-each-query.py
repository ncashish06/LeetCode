class Solution:
    # Date Solved: 13 July 2026, Monday
    # NC150
    # Refer: NeetCode, no codestorywithMIK solution available till the above date
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        """
        # Approach 1: Brute force: For each query, scan every interval and track the smallest interval that contains it.
        # Time: O(n*m) where n = intervals, m = queries
        # Space: O(1) extra (excluding output)
        result = []
        for q in queries:
            best_size = float("inf")
            for left, right in intervals:
                if left <= q <= right:
                    size = right - left + 1
                    best_size = min(best_size, size)

            if best_size != float("inf"):
                result.append(best_size)
            else:
                result.append(-1)
        return result
        """

        # Approach 2: Min-Heap (Same as NeetCode video but with comments)
        """
        Key idea: process queries in increasing order, and only "activate"
        intervals whose left endpoint is <= current query. Use a min-heap
        keyed by (size, right) so the smallest valid interval is always on top.
        Lazily remove intervals from the heap once their right endpoint
        can no longer cover the current (or any future, larger) query.
        """
        # Time: O(n*logn + m*logm) for sorting where n = intervals, m = queries
        # Space: O(n+m)

        intervals.sort(key=lambda x: x[0])

        minHeap = []  # min-heap of (interval_size, right_endpoint)
        res = {}  # maps query to its answer.
        i = 0

        # Process queries from smallest to largest.
        for q in sorted(queries):
            # Step 1: add all intervals that starts at or before q,
            # since they're now candidates for covering this (and future) queries
            while i < len(intervals) and intervals[i][0] <= q:
                left, right = intervals[i]
                size = right - left + 1
                heapq.heappush(minHeap, (size, right))
                i += 1

            # Step 2: discard intervals from the top of the heap that already
            # ended before q — they can never cover this or any larger query
            while minHeap and minHeap[0][1] < q:
                heapq.heappop(minHeap)

            # Step 3: whatever remains on top (if any) is the smallest
            # interval currently covering q
            res[q] = minHeap[0][0] if minHeap else -1

        # queries may contain duplicates or be unordered, so rebuild the
        # output in the original order using our lookup dict
        output = []
        for q in queries:
            output.append(res[q])
        return output
