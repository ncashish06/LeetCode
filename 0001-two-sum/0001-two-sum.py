class Solution:
    # Date Solved: 6 August 2026, Thursday
    # Blind 75
    # Refer: structy.net
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        """
        # For Sorted Array: Two-pointer approach.
        # Time: O(n), Space: O(1)
        left, right = 0, len(nums) - 1
        while left < right:
            current_sum = nums[left] + nums[right]
            if current_sum == target:
                return [left, right]
            elif current_sum < target:
                left += 1
            else:
                right -= 1
        return []
        """
        # For Unsorted Array: Time: O(n), Space: O(n)
        previous_nums = {}

        for index, num in enumerate(nums):
            complement = target - num

            if complement in previous_nums:
                return [previous_nums[complement], index]

            previous_nums[num] = index
