class Solution:
    # Date Solved: 23 August 2026, Sunday
    # Blind 75
    # Refer: NeetCode or codestorywithMIK
    # Also Check out: (1) LC1. Two Sum (Blind 75, Easy)
    #                 (2) LC167. Two Sum II - Input Array Is Sorted (NC150, Medium)
    #                 (3) LC18. 4Sum (NC250, Medium)
    # Time: O(n^2), Space: O(1)
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        if len(nums) < 3:
            return []

        result = []
        nums.sort()

        for i in range(len(nums) - 2):
            # since the array is sorted, once the anchor value is positive, no triplet summing to zero is possible
            if nums[i] > 0:
                break

            if i > 0 and nums[i] == nums[i - 1]:  # skip duplicates
                continue

            self.twoSum(nums, i + 1, result, -nums[i])

        return result

    def twoSum(self, nums, start, result, target) -> None:
        # Two pointer technique (Sorted array)
        left, right = start, len(nums) - 1
        while left < right:
            current_sum = nums[left] + nums[right]
            if current_sum > target:
                right -= 1
            elif current_sum < target:
                left += 1
            else:
                result.append([-target, nums[left], nums[right]])
                while left < right and nums[left] == nums[left + 1]:
                    left += 1  # skip duplicates
                while left < right and nums[right] == nums[right - 1]:
                    right -= 1  # skip duplicates
                left += 1
                right -= 1
