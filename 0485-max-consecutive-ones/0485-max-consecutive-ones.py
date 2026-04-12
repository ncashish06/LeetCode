class Solution:
    # Date Solved: 11 April 2026, Saturday
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        curr_count, max_count = 0, 0
        for i in range(len(nums)):
            if nums[i] == 0:
                max_count = max(max_count, curr_count)
                curr_count = 0
            else:
                curr_count += 1

        max_count = max(max_count, curr_count)
        return max_count
