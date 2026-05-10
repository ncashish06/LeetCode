class Solution:
    def maximumJumps(self, nums: List[int], target: int) -> int:
        n = len(nums)

        # dp[i] = max jumps to reach index n-1 FROM index i
        dp = [-1] * n       # -1 means unreachable
        dp[n - 1] = 0       # already at destination

        # Fill right to left
        for i in range(n - 2, -1, -1):
            for j in range(i + 1, n):
                # Check jump condition: value difference within target
                if -target <= nums[j] - nums[i] <= target:
                    if dp[j] != -1:     # j must itself be able to reach end
                        dp[i] = max(dp[i], 1 + dp[j])

        return dp[0]