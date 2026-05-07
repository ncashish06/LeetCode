class Solution:
    # Date Solved: 6 May 2026, Wednesday
    def maxValue(self, nums: List[int]) -> List[int]:
        n = len(nums)
        ans = [0] * n
        stack = []  # [(max_val, left_idx, right_idx)]
        for i in range(n):
            curr_max = nums[i]
            curr_left = i
            while stack and stack[-1][0] > nums[i]:
                top_max, top_left, top_right = stack.pop()
                curr_max = max(curr_max, top_max)
                curr_left = top_left
            stack.append((curr_max, curr_left, i))

        for max_val, left_idx, right_idx in stack:
            for j in range(left_idx, right_idx + 1):
                ans[j] = max_val
        return ans
