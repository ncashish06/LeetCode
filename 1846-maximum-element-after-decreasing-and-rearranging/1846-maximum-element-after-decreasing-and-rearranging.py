class Solution:
    # Date Solved: 28 June 2026, Sunday, POTD
    # Refer: codestorywithMIK, also in NeetCode All
    # Time: O(nlogn)
    def maximumElementAfterDecrementingAndRearranging(self, arr: List[int]) -> int:
        arr.sort()
        arr[0] = 1
        for i in range(1, len(arr)):
            if arr[i] - arr[i - 1] > 1:
                arr[i] = arr[i - 1] + 1

        return arr[-1]
