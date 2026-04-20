class Solution:
    def findMissingRanges(
        self, nums: List[int], lower: int, upper: int
    ) -> List[List[int]]:
        n = len(nums)
        results = []

        if n == 0:
            results.append([lower, upper])
            return results

        # Missing range at beginning
        if lower < nums[0]:
            results.append([lower, nums[0] - 1])

        for i in range(n - 1):
            if nums[i + 1] - nums[i] <= 1:
                continue
            results.append([nums[i] + 1, nums[i + 1] - 1])

        # Missing range at end
        if upper > nums[n - 1]:
            results.append([nums[n - 1] + 1, upper])

        return results
