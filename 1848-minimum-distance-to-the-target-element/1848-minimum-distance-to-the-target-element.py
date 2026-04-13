class Solution:
    # Date Solved: 12 April 2026, Sunday
    def getMinDistance(self, nums: List[int], target: int, start: int) -> int:
        min_dist = float("inf")
        for i, num in enumerate(nums):
            if num == target:
                current_dist = abs(i - start)
                min_dist = min(min_dist, current_dist)
                if min_dist == 0:
                    return 0
        return int(min_dist)
