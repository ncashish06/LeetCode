class Solution:
    # Date Solved: 10 July 2026, Friday
    # Blind 75
    # Refer: Namaste DSA
    # Time: O(nlogn) for sorting, Space: O(1)
    def eraseOverlapIntervals(self, arr: List[List[int]]) -> int:
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
