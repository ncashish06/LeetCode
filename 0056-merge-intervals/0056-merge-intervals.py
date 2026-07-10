class Solution:
    # Date Solved: 10 July 2026, Friday
    # Blind 75
    # Refer: Namaste DSA
    # Asked in Master Electronics Interview in March 2026
    def merge(self, arr: List[List[int]]) -> List[List[int]]:
        """
        Approach: Foundation for LC 759 Employee Free Time.
        LC56:  sort + merge overlapping intervals -> return merged spans
        LC759: sort + merge overlapping intervals -> return the GAPS between merged spans
        """
        arr.sort(key=lambda x: x[0])
        ans = [arr[0]]

        for i in range(1, len(arr)):
            start, end = arr[i][0], arr[i][1]
            last_end = ans[-1][1]

            if start <= last_end:
                ans[-1][1] = max(last_end, end)
            else:
                ans.append([start, end])
        return ans
