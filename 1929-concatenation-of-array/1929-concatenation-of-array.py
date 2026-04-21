class Solution:
    # Date Solved: 21 April 2026, Tuesday
    def getConcatenation(self, nums: List[int]) -> List[int]:
        n = len(nums)
        ans = [0] * 2 * n
        for idx, val in enumerate(nums):
            ans[idx] = val
            ans[idx + n] = val
        return ans
