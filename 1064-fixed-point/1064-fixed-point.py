class Solution:
    # Date Solved: 22 May 2026, Friday
    def fixedPoint(self, arr: List[int]) -> int:
        # arr[i]-i increases as i increases. We want the smallest i where arr[i]-i==0
        l, r = 0, len(arr) - 1
        res = -1

        while l <= r:
            mid = l + (r - l) // 2

            if arr[mid] == mid:
                res = mid
                r = mid - 1
            elif arr[mid] < mid:  # arr[i]-i is negative, so search right
                l = mid + 1
            else:  # arr[i]-i is positive, so search left
                r = mid - 1
        return res
