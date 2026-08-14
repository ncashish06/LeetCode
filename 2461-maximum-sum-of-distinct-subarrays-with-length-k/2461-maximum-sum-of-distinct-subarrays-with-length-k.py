class Solution:
    # Date Solved: 14 August 2026, Friday
    # Refer: codestorywithMIK
    # In NC All
    # Approach: Classic Khandani Sliding Window Template
    # Time: O(n) as each element is visited atmost twice = O(2n), don't get confused because of nested loops
    # Space: O(n) for set
    # Also see LC3090. Maximum Length Substring With Two Occurrences, 14 August 2026, Friday, POTD
    # LC2958. Length of Longest Subarray With at Most K Frequency, 12 August 2026, Wednesday, POTD
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        n = len(nums)
        seen = set()

        i = 0
        j = 0
        curr_sum = 0
        max_sum = 0

        while j < n:
            while nums[j] in seen:
                curr_sum -= nums[i]
                seen.remove(nums[i])
                i += 1

            curr_sum += nums[j]
            seen.add(nums[j])
            if j - i + 1 == k:
                max_sum = max(max_sum, curr_sum)
                curr_sum -= nums[i]
                seen.remove(nums[i])
                i += 1
            j += 1

        return max_sum
