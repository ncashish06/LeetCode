class Solution:
    # Date Solved: 24 August 2026, Monday
    # Refer: codestorywithMIK
    # Approach: Using Binary Search
    # Time: O(log(min(time) * totalTrips)), Space : O(1)
    def minimumTime(self, time: List[int], totalTrips: int) -> int:
        def possible(given_time: int) -> bool:
            actual_trips = 0
            for t in time:
                actual_trips += given_time // t
                if actual_trips >= totalTrips:
                    return True
            return actual_trips >= totalTrips

        left = 1
        right = min(time) * totalTrips

        while left < right:
            mid = left + (right - left) // 2

            if possible(mid):
                right = mid
            else:
                left = mid + 1

        return left
