class Solution:
    # Date Solved: 20 April 2026, Monday
    # Neetcode 250
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        last_seen = {}
        for i, val in enumerate(nums):
            if val in last_seen:
                if i - last_seen[val] <= k:
                    return True
            last_seen[val] = i
        return False
