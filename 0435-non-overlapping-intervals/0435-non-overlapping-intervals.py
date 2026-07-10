class Solution:
    # Date Solved: 10 July 2026, Friday
    # Blind 75
    # Time: O(nlogn) for sorting, Space: O(1)
    def eraseOverlapIntervals(self, arr: List[List[int]]) -> int:
        """
        # Approach 1: Sort by end
        # Refer: NeetCode, Namaste DSA
        arr.sort(key=lambda x: x[1])
        remove_count = 0
        prev_end = arr[0][1]
        for i in range(1, len(arr)):
            start, end = arr[i][0], arr[i][1]
            if (start < prev_end):  # Golden rule to check overlap: current_start <= last_end
                remove_count += 1
            else:
                prev_end = end
        return remove_count
        """
        # Approach 2: Sort by start
        # Refer: NeetCode
        arr.sort(key=lambda x: x[0])
        remove_count = 0
        prev_end = arr[0][1]
        for i in range(1, len(arr)):
            start, end = arr[i][0], arr[i][1]
            if (start < prev_end):  # Golden rule to check overlap: current_start <= last_end
                remove_count += 1
                prev_end = min(end, prev_end)  # GREEDY: Keep only the interval which ends early as said by NamasteDSA
            else:
                prev_end = end
        return remove_count
