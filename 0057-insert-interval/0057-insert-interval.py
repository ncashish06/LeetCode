class Solution:
    # Date Solved: 9 July 2026, Thursday
    # Blind 75
    # Refer: Namaste DSA and codestorywithMIK
    # Time: O(n), Space: O(n) for ans array
    def insert(self, arr: List[List[int]], x: List[int]) -> List[List[int]]:
        n = len(arr)
        ans = []
        i = 0
        # when arr = [[1,2]] and x=[3,4], ans.append(x) after the overlapping intervals block adds [3,4]
        # left non-overlapping intervals
        while i < n and arr[i][1] < x[0]:
            ans.append(arr[i])
            i += 1

        # overlapping intervals
        while i < n and arr[i][0] <= x[1]:
            x[0] = min(x[0], arr[i][0])
            x[1] = max(x[1], arr[i][1])
            i += 1
        ans.append(x)

        # right non-overlapping intervals
        while i < n:
            ans.append(arr[i])
            i += 1
        return ans
