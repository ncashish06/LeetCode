class Solution:
    # Date Solved: 23 August 2026, Sunday
    # Blind 75
    # Refer: structy.net
    # Also Check out: (1) LC167. Two Sum II - Input Array Is Sorted (NC150, Medium)
    #                 (2) LC15. 3Sum (Blind 75, Medium)
    #                 (3) LC18. 4Sum (NC250, Medium)
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # Time: O(n), Space: O(n)
        previous_nums = {}

        for index, num in enumerate(nums):
            complement = target - num

            if complement in previous_nums:
                return [previous_nums[complement], index]

            previous_nums[num] = index
