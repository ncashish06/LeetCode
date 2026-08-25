class Solution:
    # Date Solved: 25 August 2026, Tuesday, POTD
    # Refer: LeetCode Editorial
    # Time: O(n), Space: O(n)
    def missingMultiple(self, nums: List[int], k: int) -> int:
        seen = set(nums)
        ans = k
        while ans in seen:
            ans += k
        return ans
