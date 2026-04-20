class Solution:
    # Date Solved: 20 April 2026, Monday
    # Blind 75
    def containsDuplicate(self, nums: List[int]) -> bool:
        last_seen = set()
        for num in nums:
            if num in last_seen:
                return True
            last_seen.add(num)
        return False
