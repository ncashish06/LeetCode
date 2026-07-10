class Solution:
    # Date Solved: 10 July 2026, Friday
    # In NC All under Intervals topic
    # Time: O(n), Space: O(1)
    def removeInterval(self, arr: List[List[int]], toBeRemoved: List[int]) -> List[List[int]]:
        ans = []
        remove_start, remove_end = toBeRemoved[0], toBeRemoved[1]

        for i in range(len(arr)):
            start, end = arr[i][0], arr[i][1]

            if end <= remove_start or start >= remove_end:
                # SAFE: no overlap at all, keep interval as-is
                ans.append([start, end])
            else:
                # OVERLAP — keep only the non-overlapping portions
                if start < remove_start:  # Is there a left interval we need to keep?
                    ans.append([start, remove_start])
                if end > remove_end:  # Is there a right interval we need to keep?
                    ans.append([remove_end, end])

        return ans
