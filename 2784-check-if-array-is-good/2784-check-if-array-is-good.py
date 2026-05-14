class Solution:
    # Date Solved: 13 May 2026, Wednesday
    def isGood(self, nums: List[int]) -> bool:
        maxVal = max(nums)
        if len(nums) < maxVal + 1:
            return False
        nums.sort()
        for i in range(len(nums) - 1):
            if nums[i] != i + 1:
                return False
        return nums[-1] == nums[-2]
