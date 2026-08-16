class Solution:
    # Date Solved: 15 August 2026, Saturday
    # Refer: codestorywithMIK, NC's approach is same
    # NC250
    # Approach: Classic Khandani Sliding Window Template
    # Time: O(n) as each element is visited atmost twice = O(2n), don't get confused because of nested loops
    # Space: O(1)
    # LC862. Shortest Subarray with Sum at Least K (Hard, in NC all) allows negative integers where this approach won't work. Heap/Stack used there.
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        n = len(nums)
        i, j = 0, 0
        curr_sum = 0
        min_len = float("inf")

        while j < n:
            curr_sum += nums[j]

            while curr_sum >= target:
                min_len = min(min_len, j - i + 1)
                curr_sum -= nums[i]
                i += 1

            j += 1

        return 0 if min_len == float("inf") else min_len
