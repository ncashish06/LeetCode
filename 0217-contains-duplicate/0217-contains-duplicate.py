class Solution:
    # Date Solved: 20 April 2026, Monday
    # Blind 75
    def containsDuplicate(self, nums: List[int]) -> bool:
        last_seen = {}
        for i, val in enumerate(nums):
            if val in last_seen:
                return True
            last_seen[val] = i
        return False
