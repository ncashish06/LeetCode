class Solution:
    # Date Solved: 12 August 2026, Wednesday, POTD
    # Refer: codestorywithMIK, NC's approach is same
    # In NC All
    # Approach: Classic Khandani Sliding Window Template
    # Time: O(n) as each element is visited atmost twice = O(2n), don't get confused because of nested loops
    # Space: O(n)
    # Also see LC3090. Maximum Length Substring With Two Occurrences, 14 August 2026, Friday, POTD
    def maxSubarrayLength(self, nums: List[int], k: int) -> int:
        n = len(nums)
        mp = defaultdict(int)

        i = 0
        j = 0
        result = 0

        while j < n:

            mp[nums[j]] += 1

            while i < j and mp[nums[j]] > k:
                mp[nums[i]] -= 1
                i += 1

            result = max(result, j - i + 1)
            j += 1

        return result
