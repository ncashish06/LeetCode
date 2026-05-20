class Solution:
    # Date Solved: 19 May 2026, Tuesday
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        """
        Approach: Foundation for LC 759 Employee Free Time.
        LC56:  sort + merge overlapping intervals → return merged spans
        LC759: sort + merge overlapping intervals → return the GAPS between merged spans
        """
        intervals.sort(key=lambda pair: pair[0])
        output = [intervals[0]]

        for start, end in intervals:
            lastEnd = output[-1][1]

            if start <= lastEnd:
                output[-1][1] = max(lastEnd, end)
            else:
                output.append([start, end])
        return output
