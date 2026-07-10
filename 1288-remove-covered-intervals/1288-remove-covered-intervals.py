class Solution:
    # Date Solved: 6 July 2026, Monday, POTD
    # Refer: codestorywithMIK. Also, in NC All with video explanation.
    # Good "Intervals" topic question for practice which will help with other "Intervals" Blind 75, NC150 problems.
    def removeCoveredIntervals(self, arr: List[List[int]]) -> int:
        """
        # Approach 1: Using O(n) space and sorting. Time : O(nlogn), Space : O(n)
        arr.sort(key=lambda x: (x[0], -x[1]))
        ans = [arr[0]]
        for i in range(1, len(arr)):
            start, end = arr[i][0], arr[i][1]
            prev_start, prev_end = ans[-1][0], ans[-1][1]
            if prev_start <= start and prev_end >= end: # current interval is completely inside previous, so don't add
                continue
            ans.append(arr[i])
        return len(ans)

        # Approach 2: Using O(n) space and sorting + Simplified condition check. Time : O(nlogn), Space : O(n)
        arr.sort(key=lambda x: (x[0], -x[1]))
        ans = [arr[0]]
        for i in range(1, len(arr)):
            end = arr[i][1]
            prev_end = ans[-1][1]
            # Simplified, As ans[-1][0] <= start is always true and is redundant (due to sorting)
            if prev_end >= end: # current interval is completely inside previous, so don't add
                continue
            ans.append(arr[i])
        return len(ans)
        """
        # Approach 3: Using constant space and sorting. Time : O(nlogn), Space : O(1)
        arr.sort(key=lambda x: (x[0], -x[1]))
        prev_end = arr[0][1]
        count = 1
        for i in range(1, len(arr)):
            start, end = arr[i][0], arr[i][1]
            if prev_end >= end:
                continue
            prev_end = end
            count += 1
        return count
