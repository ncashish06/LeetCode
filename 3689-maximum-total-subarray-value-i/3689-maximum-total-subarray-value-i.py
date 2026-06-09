class Solution:
    # Date Solved: 9 June 2026, Tuesday, POTD
    def maxTotalValue(self, nums: List[int], k: int) -> int:
        max_elem, min_elem = max(nums), min(nums)
        return k * (max_elem - min_elem)
