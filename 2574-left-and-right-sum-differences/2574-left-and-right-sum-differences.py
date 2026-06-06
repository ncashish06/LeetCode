class Solution:
    # Date Solved: 6 June 2026, Saturday, POTD
    # Similar to LC.238 Product of Array Except Self
    def leftRightDifference(self, nums: List[int]) -> List[int]:
        total_sum = sum(nums)
        curr = 0
        res = []
        for i in range(len(nums)):
            left_sum = curr
            curr += nums[i]
            right_sum = total_sum - curr
            res.append(abs(right_sum - left_sum))
        return res
