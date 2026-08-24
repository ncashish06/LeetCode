class Solution:
    # Date Solved: 23 August 2026, Sunday
    # NC150
    # Refer: structy.net
    # Also Check out: (1) LC1. Two Sum (Blind 75, Easy)
    #                 (2) LC15. 3Sum (Blind 75, Medium)
    #                 (3) LC18. 4Sum (NC250, Medium)
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # 2-pointers: Time: O(n), Space: O(1)
        # There is also binary search approach which looks for the complement but takes O(nlogn) time.
        left, right = 0, len(numbers) - 1
        while left < right:
            current_sum = numbers[left] + numbers[right]
            if current_sum == target:
                return [left + 1, right + 1]
            elif current_sum < target:
                left += 1
            else:
                right -= 1
        return []
