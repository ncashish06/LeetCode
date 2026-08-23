class Solution:
    # Date Solved: 23 August 2026, Sunday
    # In NC All
    # Refer: NeetCode and codestorywithMIK
    # Asked recently in Infosys OA
    # Time: O(3^n) with only recursion, O(n) with Memoization, Space: O(1)
    def validPartition(self, nums: List[int]) -> bool:
        n = len(nums)
        t = [-1] * (n + 1)
        t[n] = True

        def solve(i):
            if t[i] != -1:
                return t[i]

            res = False
            if i < len(nums) - 1 and nums[i] == nums[i + 1]:
                res = solve(i + 2)
            if i < len(nums) - 2:
                if (nums[i] == nums[i + 1] == nums[i + 2]) or (
                    nums[i] + 1 == nums[i + 1] and nums[i + 1] + 1 == nums[i + 2]
                ):
                    res = res or solve(i + 3)

            t[i] = res
            return res

        return solve(0)
