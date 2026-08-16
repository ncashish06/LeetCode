class Solution:
    # Date Solved: 16 August 2026, Sunday
    # Refer: codestorywithMIK
    # In NC All
    # Approach: Classic Khandani Sliding Window Template
    # Time: O(n) as each element is visited atmost twice = O(2n), don't get confused because of nested loops
    # Space: O(1)
    def countSubarrays(self, nums: List[int], k: int) -> int:
        maxE = max(nums)

        n = len(nums)
        i = j = 0

        result = 0
        countMax = 0

        while j < n:
            if nums[j] == maxE:
                countMax += 1

            while countMax >= k:
                result += n - j

                if nums[i] == maxE:
                    countMax -= 1
                i += 1

            j += 1

        return result
