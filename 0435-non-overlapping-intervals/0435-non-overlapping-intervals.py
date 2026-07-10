class Solution:
    # Date Solved: 10 July 2026, Friday
    # Blind 75
    # Time: O(nlogn) for sorting, Space: O(1)
    def eraseOverlapIntervals(self, arr: List[List[int]]) -> int:
        # Approach 1: sort by end
        # Refer: Namaste DSA
        arr.sort(key=lambda x: x[1])
        remove_count = 0
        k = float("-inf")
        for i in range(len(arr)):
            start, end = arr[i][0], arr[i][1]
            if start < k:  # Golden rule to check overlap: current_start <= last_end
                remove_count += 1
            else:
                k = end
        return remove_count
        """
        # Approach 2: sort by start
        # Refer: codestorywithMIK
        arr.sort(key=lambda x: x[0])
        n = len(arr)
        count = 0
        i, j = 0, 1

        while j < n:
            curr_start, curr_end = arr[i][0], arr[i][1]
            next_start, next_end = arr[j][0], arr[j][1]

            if curr_end <= next_start:  # SAFE — no overlap
                i = j
                j += 1
            elif curr_end <= next_end:
                # GREEDY: remove next interval, it has high chance of overlapping with future intervals
                j += 1
                count += 1
            else:  # curr_end > next_end
                # GREEDY: remove current interval, it has high chance of overlapping with future intervals
                i = j
                j += 1
                count += 1

        return count
        """
